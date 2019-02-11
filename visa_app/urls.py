"""visa_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from app import views

urlpatterns = [
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    re_path(r'^form1', views.form1),
    re_path(r'^form2', views.form2),
    re_path(r'^all_forms', views.all_forms),
    re_path(r'^add_member', views.add_member),
    #re_path(r'form2', views.form2),
    #re_path(r'^about/contact/', views.contact),
    #re_path(r'^about', views.about),
    path(r'', views.index),
]