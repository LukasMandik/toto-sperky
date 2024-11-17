from django.http import HttpResponseForbidden
import re
import logging

security_logger = logging.getLogger('django.security')

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.suspicious_patterns = [
            r'\.env',
            r'\.php',
            r'wp-',
            r'admin',
            r'\.sql',
            r'phpMyAdmin',
            r'\.git',
            r'\.htaccess',
            r'\.asp',
            r'\.jsp'
        ]

    def __call__(self, request):
        # Kontrola podozrivých URL
        path = request.path.lower()
        ip = self.get_client_ip(request)
        
        for pattern in self.suspicious_patterns:
            if re.search(pattern, path):
                self.log_suspicious_request(request, ip, pattern)
                return HttpResponseForbidden("Access Denied")

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

    def log_suspicious_request(self, request, ip, pattern):
        log_data = {
            'ip': ip,
            'path': request.path,
            'method': request.method,
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'pattern': pattern,
            'referer': request.META.get('HTTP_REFERER', '')
        }
        security_logger.warning(f"Suspicious request detected: {log_data}")