from django import template
from collections import Counter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sort_dict(dictionary):
    text = ""
    hashtags = Counter(dictionary)
    hashtags = hashtags.most_common()
    for item in hashtags:
    	string = "<li><span>%s: </span><span>%d</span></li>" % (item[0], item[1])
    	text += string
    return mark_safe(text)