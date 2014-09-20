from meapp.views import kk,delete,tj,aaj,main,ajax,rqid,aj2main,aj2,showlay
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('pp',
    url(r'^rqid$',rqid,name='rqid'),
    url(r'^kk$',kk,name='inin'),
    url(r'^delete$',delete,name='delete'),
    url(r'^tj$',tj,name='tj'),
    url(r'^aaj$',aaj,name='aaj'),
    # url(r'^ooaj$',ooaj,name='ooaj'),
    # url(r'^ajaxexample$', 'meapp.views.main'),
    # url(r'^ajaxexample_json$', 'meapp.views.ajax'),
    url(r'^ajaxexample$', main,name='main'),
    url(r'^ajaxexample_json$', ajax,name='ajax'),
    url(r'^aj2main$', aj2main,name='aj2main'),
    url(r'^aj2$', aj2,name='aj2'),
    url(r'^showlay$', showlay,name='showlay'),
    )