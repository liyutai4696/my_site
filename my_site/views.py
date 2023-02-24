from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def select_index(request):
    return HttpResponseRedirect('select_index/')

def select_html(request):
    return render(request,'select_index.html')