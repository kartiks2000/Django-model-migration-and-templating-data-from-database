# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Topic,AccessRecord,Webpage

# Create your views here.
def intro(request):
    myweblist = AccessRecord.objects.order_by('date')
    d = {'myl':myweblist}
    return render(request,'index1.html',context=d)
