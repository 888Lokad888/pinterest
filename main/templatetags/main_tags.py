from django import template
from random import choice
from main.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()

@register.simple_tag
def count_tags(tag):
    return len(Post.objects.filter(is_published=True).filter(tags__name=tag))

@register.simple_tag
def random_post():
    return choice(Post.objects.filter(is_published=True)).get_absolute_url()
