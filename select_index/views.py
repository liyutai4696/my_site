from django.shortcuts import render

# Create your views here.

def select_index(request):
    
    return render(request,'select_index.html')