"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Includ+Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from design.views import *
from vage.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',home,name= "home"),
    # path('about/',about,name= "about"),
    # path('service/',service,name= "service"),

    path('design/',design,name='design'),
    path('receipes/',receipes,name='receipes'),
    path('delete/<int:id>/',delete,name="delete"),
    path('update/<int:id>/',update,name="update"),
    path('form/',form,name='form'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('demo/',demo,name="demo"),

    path('RAGISTER/',RAGISTER,name="RAGISTER"),
    path('hed/',hed,name="hed"),
    path('shreya/',shreya,name='shreya'),
    path('ptns/',ptns,name='ptns'),
    path('loginptn/',loginptn,name='loginptnp'),
    path('delete_pts/<int:id>/',delete_pts,name="delete_pts"),

    path('session/',session),
    path('get/',get),
    path('logout/',logout),
    
    path('loginhp/',loginhp,name='loginhp'),
    path('loginfrm/',loginfrm,name='loginfrm')
    




    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
