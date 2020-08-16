# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import Topic,Webpage,AccessRecord

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
