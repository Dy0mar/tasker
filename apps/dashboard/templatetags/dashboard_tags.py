# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.filter
def replacer(string):
    try:
        return string.title().replace('-', ' ')
    except AttributeError:
        return string
