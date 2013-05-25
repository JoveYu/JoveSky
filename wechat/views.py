# -*- coding: utf-8 -*-
"""
File: views.py
Author: Jove Yu
Email: yushijun110@gmail.com
Github: https://github.com/JoveYu
Description: view for wechat app
"""

from django.http import HttpResponse
from django.template import RequestContext,Template
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import hashlib

WECHAT_TOKEN=getattr(settings,'WECHAT_TOKEN')

@csrf_exempt
def index(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
        return HttpResponse('Hello World')
    return HttpResponse('Hello World')

def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    token=WECHAT_TOKEN

    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None

