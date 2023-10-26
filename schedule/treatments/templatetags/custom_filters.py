from django import template
from django.template.defaultfilters import truncatewords_html

register = template.Library()

@register.filter(name='truncate_30_words')
def truncate_300_words(value):
    return truncatewords_html(value, 30)
