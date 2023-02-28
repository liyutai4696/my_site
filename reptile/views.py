from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError,HTTPError
import http.cookiejar, urllib.request
from urllib.parse import urlparse
import os

import requests
import re


from my_site.settings import BASE_DIR

def test1(request):

    r = requests.get('https://www.httpbin.org/get')
    print(type(r.text))
    print(r.json())
    print(type(r.json()))
   
    return HttpResponse(r.text)

def test2(request):
    r = requests.get('https://ssr1.scrape.center/')
    pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
    titles = re.findall(pattern,r.text)
    print(titles)

    return HttpResponse(titles)

def test3(request):
    filename = os.path.join(BASE_DIR,'cookie.txt')
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    
    cookie.save(ignore_discard=True,ignore_expires=True)

    return HttpResponse('访问成功')

def test4(request):
    try:
        response = urllib.request.urlopen('https://cuiqingcai.com/404')
        print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
        return HttpResponse('访问失败1')
    except URLError as e:
        print(e.reason)
        return HttpResponse('访问失败2')

    return HttpResponse(response.read().decode('utf-8'))

def test5(request):
    result = urlparse('https://www.baiduc.com/index.html;user?id=5#comment')
    print(type(result))
    print(result)

    return HttpResponse(result)
