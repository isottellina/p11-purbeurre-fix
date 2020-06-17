# gravatar.py --- 
# 
# Filename: gravatar.py
# Author: Louise <louise>
# Created: Wed Jun 17 19:42:18 2020 (+0200)
# Last-Updated: Wed Jun 17 19:59:50 2020 (+0200)
#           By: Louise <louise>
# 
import hashlib
from urllib.parse import urlencode
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def gravatar_url(email, size=40):
    """
    Returns the Gravatar URL for a given email.
    """
    return "https://www.gravatar.com/avatar/{user_hash}?{parameters}".format(
        user_hash=hashlib.md5(email.lower().encode()).hexdigest(),
        parameters=urlencode({'s':str(size)})
    )
