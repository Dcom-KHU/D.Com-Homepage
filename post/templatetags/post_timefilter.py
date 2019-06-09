from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def time_ego_to_korean(value):
    list_var = value.split(',')
    time_var = list_var[0].split()

    if time_var[1] == 'minute' or time_var[1] == 'minutes':
        time_var[1] = '분 전'
    elif time_var[1] == 'hour' or time_var[1] == 'hours':
        time_var[1] = '시간 전'
    elif time_var[1] == 'day' or time_var[1] == 'days':
        time_var[1] = '일 전'
    elif time_var[1] == 'week' or time_var[1] == 'weeks':
        time_var[1] = '주 전'
    elif time_var[1] == 'month' or time_var[1] == 'months':
        time_var[1] = '달 전'
    elif time_var[1] == 'year' or time_var[1] == 'years':
        time_var[1] = '년 전'

    return time_var[0] + time_var[1]


time_ego_to_korean.is_safe = True
