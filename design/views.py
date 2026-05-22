from django.shortcuts import render
from .models import *

# Create your views here.

# def design(request):
#     return render(request,design)
# def about(request):
#     return render(request,"about.html")
# def home(request):
#     return render(request,"home.html")
# def service(request):
#     return render(request,"service.html")
    
from django.http import HttpResponse
def design(request):
    peoples=[
        
        {'name':'ashish','age':20},
        {'name':'mansi','age':20},
        {'name':'shreya','age':18},
        {'name':'monu','age':10},        
    ]
    
    
    return render(request,"table.html",context={'peoples':peoples})







