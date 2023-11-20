from django import template
from django.template.defaultfilters import truncatewords_html

register = template.Library()

@register.filter(name='truncate_30_words')
def truncate_300_words(value):
    return truncatewords_html(value, 30)

@register.filter(name="last_item")
def last_item(queryset):
    if queryset:
        return queryset.last()
    return None

@register.filter(name="first_item")
def first_item(queryset):
    if queryset:
        return queryset.first()
    return None
