__author__ = 'Morya Jr'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from projectidea import views

urlpatterns = [
    url(r'^$', views.idea_list, name='idea_list'),
    url(r'^tech/$', views.technology_list, name='technology_list'),
    url(r'^envr/$', views.environment_list, name='environment_list'),
    url(r'^shopping/$', views.shopping_list, name='shopping_list'),
    url(r'^people/$', views.people_list, name='people_list'),
    url(r'^financial/$', views.financial_list, name='financial_list'),
    url(r'^writing/$', views.writing_list, name='writing_list'),
    url(r'^ideas/(?P<pk>[0-9]+)/$', views.idea_detail, name='idea_detail'),
    url(r'^ideas/new/$', views.idea_new, name='idea_new'),
    url(r'^ideas/(?P<pk>[0-9]+)/edit/$', views.idea_edit, name='idea_edit'),
    url(r'^ideas/(?P<pk>[0-9]+)/remove/$', views.idea_remove, name='idea_remove'),
    url(r'^ideaapi/$', views.IdeasList.as_view()),
    url(r'^ideaapi/(?P<pk>[0-9]+)/$', views.IdeaDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)