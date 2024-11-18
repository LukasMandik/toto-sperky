from django.http import HttpResponseForbidden, HttpResponse
import re
import logging
from django.core.exceptions import PermissionDenied
from django.conf import settings

security_logger = logging.getLogger('django.security')

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Pridajte povolené user agents
        self.allowed_user_agents = [
            'sentryuptimebot',
            'sentry'
        ]
        
        # Rozšírený zoznam blokovaných vzorov
        self.blocked_patterns = [
            # Systémové a konfiguračné súbory
            r'\.env',
            r'\.git',
            r'\.htaccess',
            r'\.bash_history',
            r'\.ssh',
            r'\.config',
            r'\.profile',
            r'\.log',
            
            # Databázové a zálohovacie súbory
            r'\.sql',
            r'\.bak',
            r'\.backup',
            r'\.dump',
            r'\.db',
            
            # Skripty a citlivé koncovky
            r'\.php',
            r'\.asp',
            r'\.aspx',
            r'\.jsp',
            r'\.cgi',
            r'\.exe',
            r'\.sh',
            r'\.bash',
            
            # WordPress a CMS
            r'wp-',
            r'wordpress',
            r'wp-admin',
            r'wp-login',
            r'wp-content',
            
            # Admin a správa
            r'admin',
            r'administrator',
            r'phpMyAdmin',
            r'phpmyadmin',
            r'mysql',
            r'database',
            
            # API a konfigurácia
            r'api',
            r'config',
            r'configuration',
            r'setup',
            r'install',
            
            # Systémové príkazy
            r'exec',
            r'shell',
            r'cmd',
            r'command',
            
            # Média processing
            r'ffmpeg',
            r'convert',
            
            # Ostatné nebezpečné vzory
            r'level',
            r'proxy',
            r'passwd',
            r'password',
            r'admin',
            r'root',
            
            # Docker API endpoints
            r'containers',
            r'images',
            r'volumes',
            r'networks',
            r'swarm',
            r'nodes',
            r'services',
            r'tasks',
            r'secrets',
            r'configs',
            r'docker',
            
            # Systémové a diagnostické endpointy
            r'version',
            r'info',
            r'_ping',
            r'events',
            r'system',
            r'stats',
            r'top',
            r'processes',
            
            # FFmpeg a média
            r'ffmpeg',
            r'ffprobe',
            r'stream',
            r'convert',
            r'media',
            
            # Ďalšie nebezpečné cesty
            r'debug',
            r'test',
            r'setup',
            r'install',
            r'config',
            r'settings'
        ]
        
        # IP adresy, ktoré chceme blokovať
        self.blocked_ips = set([
            # Môžete pridať konkrétne IP adresy
        ])
        
        # Povolené domény
        self.allowed_hosts = {
            'totosperky.sk',
            'www.totosperky.sk',
            'localhost',
            '127.0.0.1'
        }

    def __call__(self, request):
        # Kontrola IP adresy
        client_ip = self.get_client_ip(request)
        if client_ip in self.blocked_ips:
            self.log_attack(request, client_ip, "blocked_ip")
            return HttpResponseForbidden("Access Denied")

        # Kontrola hostu
        if not self.is_valid_host(request):
            self.log_attack(request, client_ip, "invalid_host")
            return HttpResponseForbidden("Invalid Host")

        # Kontrola podozrivých URL
        path = request.path.lower()
        for pattern in self.blocked_patterns:
            if re.search(pattern, path):
                self.log_attack(request, client_ip, f"blocked_pattern: {pattern}")
                return HttpResponseForbidden("Access Denied")

        # Kontrola user agenta
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if not user_agent or 'ffmpeg' in user_agent:
            self.log_attack(request, client_ip, "suspicious_user_agent")
            return HttpResponseForbidden("Access Denied")

        return self.get_response(request)

    def is_valid_host(self, request):
        host = request.get_host().split(':')[0].lower()
        return host in self.allowed_hosts

    def is_suspicious_request(self, request):
        path = request.path.lower()
        for pattern in self.blocked_patterns:
            if re.search(pattern, path):
                return True
        return False

    def is_suspicious_user_agent(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        
        # Najprv skontrolujte povolené user agents
        if any(agent in user_agent for agent in self.allowed_user_agents):
            return False
            
        suspicious_agents = [
            'sqlmap',
            'nikto',
            'nmap',
            'masscan',
            'python-requests',
            'wget',
            'curl',
            'postman',
            'bot',
            'scanner'
        ]
        return any(agent in user_agent for agent in suspicious_agents)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')

    def log_attack(self, request, ip, attack_type):
        log_data = {
            'ip': ip,
            'path': request.path,
            'method': request.method,
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'attack_type': attack_type,
            'host': request.get_host(),
            'query_string': request.META.get('QUERY_STRING', ''),
            'referer': request.META.get('HTTP_REFERER', '')
        }
        security_logger.warning(f"Attack attempt detected: {log_data}") 