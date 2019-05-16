from django import template
import datetime
register = template.Library()

#@register.filter(name='isenabled')
@register.simple_tag
def isenabled(value):
    temp= value - datetime.date.today()
    if temp.days == 0 or temp.days == 1:
        return True
    else:
        return False
