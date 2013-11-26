

import os

from django.utils.timezone import now
from django.conf import settings
from django.db import models

def _add_leading_zero_to_date (date_value) :
    date_value = str(date_value)
    if len(date_value) < 2 :
        date_value = '0' + date_value
    return date_value

def _pretty_date (datetime, template='{year}-{month}-{day}') :
    return template.format(year=str(datetime.year),
                           month=_add_leading_zero_to_date(datetime.month),
                           day=_add_leading_zero_to_date(datetime.day))

class Image (models.Model) :
    name        = models.CharField(max_length=1000)
    author      = models.CharField(max_length=1000, blank=True, default=settings.BLOG.AUTHOR)
    date        = models.DateTimeField(default=now)
    image       = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    def __str__ (self) :
        return '%s <%s>' % (self.name, self.image)

class Article (models.Model) :
    title          = models.CharField(max_length=1000)
    author         = models.CharField(max_length=1000, blank=True, default=settings.BLOG.AUTHOR)
    thumbnail      = models.ForeignKey(Image, blank=True, null=True)
    show_thumbnail = models.BooleanField(default=True)
    date           = models.DateTimeField(default=now)
    summary        = models.TextField(blank=True)
    body           = models.TextField()

    def url (self) :
        return '/articles/%s' % str(self.id)

    def pretty_date (self) :
        return _pretty_date(self.date)

