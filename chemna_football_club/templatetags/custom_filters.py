import base64
from django import template

register = template.Library()

@register.filter
def urlsafe_base64(value):
    return base64.urlsafe_b64encode(value.encode('utf-8')).decode('utf-8')