from django import template

register = template.Library()

def linecount(value):
    total_chars = len(value)
    whitespace_chars = sum(1 for char in value if char.isspace())
    return {
        'total_chars': total_chars,
        'whitespace_chars': whitespace_chars,
    }