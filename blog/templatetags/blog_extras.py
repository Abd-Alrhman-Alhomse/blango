from django import template
from django.utils.html import escape,format_html
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, user=None):
  if not isinstance(author, user_model):
    return ""

  if author == user :
    return format_html("<strong>me</strong>")
  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = f'{author.username}'
  
  if author.email :
    ml  = author.email
    pre = format_html('<a href="mailto:{}">', ml)
    suf = format_html("</a>")
  else :
    pre = ""
    suf = ""
  return format_html("{}{}{}",pre,name,suf)


