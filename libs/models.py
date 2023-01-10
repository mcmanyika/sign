# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class t_sign(models.Model):
    title = models.CharField(max_length=50, default='', null=True, blank=True)
    description = models.TextField()
    dateFrom = models.DateField(null=True, blank=True)
    dateTo = models.DateField(null=True, blank=True)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title