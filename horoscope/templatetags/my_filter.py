from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)


@register.filter(name='times')
def times(count):
    lst = []
    for i in range(count):
        lst.append(i)
    return lst


@register.filter(name='filter_range')
def filter_range(begin, end):
    lst = []
    for i in range(begin, end):
        lst.append(i)
    return lst
