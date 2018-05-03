#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 17:12:31
# @Author  : chie (liqianhui@ledongli.me)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
