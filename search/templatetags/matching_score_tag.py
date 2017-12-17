from django import template
register = template.Library()

@register.simple_tag
def matching_score(max_score, score):
    return int((score/max_score)*100)