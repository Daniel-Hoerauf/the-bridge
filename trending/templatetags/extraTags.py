from django import template
from collections import Counter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sort_hashtags(dictionary):
    text = ""
    hashtags = Counter(dictionary)
    hashtags = hashtags.most_common()
    for item in hashtags:
    	string = "<li><span><a href='https://twitter.com/hashtag/%s'>%s</a>: </span><span>%d</span></li>" % (item[0], item[0], item[1])
    	text += string
    return mark_safe(text)

@register.filter
def sort_mentions(dictionary):
    text = ""
    mentions = Counter(dictionary)
    mentions = mentions.most_common()
    for item in mentions:
    	string = "<li><span><a href='https://twitter.com/%s'>%s</a>: </span><span>%d</span></li>" % (item[0], item[0], item[1])
    	text += string
    return mark_safe(text)