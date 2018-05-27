#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 17:12:31
# @Author  : chie (liqianhui@ledongli.me)

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'upload_file/$', views.upload_file, name='upload_file'),
    url(r'get_txt/$', views.get_txt, name='get_txt')
]
