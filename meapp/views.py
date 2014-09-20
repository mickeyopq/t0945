#coding: utf-8 -*-
from django.core import serializers
import json
from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponse
from meapp.models import Pgg
import datetime
from django.http import *
from django.template import RequestContext
import socket
# from django.utils import simplejson
import json as simplejson
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})
def aj2main(request):
    return render_to_response('aj2main.html')
def aj2(request):
    obj = {"a": 1, "b": 2}
    obj_as_json = serializers.serialize("json", my_model_object)
    data = {'foo': 'bar', 'hello': 'world'}
    return HttpResponse(json.dumps(data), content_type='application/json')
def main(request):
   return render_to_response('ajaxexample.html', context_instance=RequestContext(request))

def ajax(request):
    if request.POST.has_key('client_response'):
        x = request.POST['client_response']+"FQ AJAX"                  
        # y = socket.gethostbyname(x)                           
        # response_dict = {}                                          
        # response_dict.update({'server_response': y })                                                                   
        return HttpResponse("FFFFQ"+x) 
        # return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript') 
    else:
        print "ELSE ELSE;;;;;;;;;"
        return render_to_response('ajaxexample.html', context_instance=RequestContext(request))



# Create your views here.
def rqid(request):
#ajax那邊    
    if request.GET.has_key('client_response'):
        id = request.GET['client_response']                  
        paa=Pgg.objects.get(id=id)
        return HttpResponse(paa,content_type="application/json")
    else:
        print "ELSE ELSE;;;;;;;;;"
        return HttpResponse("NGNGNGNGNG")
        # return render_to_response('showtj.html'
        #     ,{'yy':'ERROOOORR'}
        #     , context_instance=RequestContext(request))
#delete那邊    
    if request.method== 'GET':
        try:
            id = request.GET['mid']
            aa=Pgg.objects.get(id=id)
            aa.delete()
        except Exception, e:
            pass
    return render_to_response('fq.html'
        ,{'pps':ls()}
        )

def ls():
    pps = Pgg.objects.all()
    pps=pps.extra(order_by = ['-id'])
    return pps
def kk(request):
    if request.method == 'GET':
        try:
            dd= Pgg()
            dd.tel=request.GET['tel']
            dd.save()
        except Exception, e:
            pass
    return render_to_response('fq.html'
        ,{'pps':ls()}
        ,context_instance=RequestContext(request)
        )


def delete(request):
    if request.method== 'GET':
        try:
            id = request.GET['mid']
            aa=Pgg.objects.get(id=id)
            aa.delete()
        except Exception, e:
            pass
    return render_to_response('fq.html'
        ,{'pps':ls()}
        )
    # return HttpResponse(aa)
def tj(request):
    return render_to_response('showtj.html')

def aaj(request):
    # if request.method== 'GET':
    if request.GET.has_key('client_response'):
        x = request.GET['client_response']                  
        x+=";;;;;;;;;GOOD:::"
        return HttpResponse(x) 
    else:
        print "ELSE ELSE;;;;;;;;;"
        return render_to_response('showtj.html'
            ,{'yy':'ERROOOORR'}
            , context_instance=RequestContext(request))
def showlay(request):
    return render_to_response('showlay.html')