# this should be at the top of your custom template tags file
from datetime import datetime

from django.template import Library
from django.conf import settings

register = Library()


# custom template filter - place this in your custom template tags file
@register.filter
def my_timeSince(value):
    """
    Filter - removes the minutes, seconds, and milliseconds from a datetime

    Example usage in template:

    {{ my_datetime|my_timeSince }}

    This would show the hours in my_datetime without showing the minutes or seconds.
    """
    # replace returns a new object instead of modifying in place
    value = value
    day_log = str(datetime.now() - value)

    if 'day' in day_log:
        return str(int(day_log.split('day')[0])) + 'days ago'
    # elif
    else:
        all_log = day_log.split(':')
        if str(int(all_log[0])) != '0':
            return all_log[0] + 'hours ago'
        else:
            if int(all_log[1]) < 10:
                return 'Just Now'
            return str(int(all_log[1])) + 'mins ago'


@register.filter
def imgSrc(value):
    if str(value) != '':
        if 'http' in str(value):
            return str(value)
        else:
            return settings.MEDIA_URL + str(value)
    else:
        return settings.STATIC_URL + 'images/news_default.png'
