from django.contrib import admin
from django.urls import path,re_path

from app import views

urlpatterns = [
    #path('edit/<int:id>/', views.edit),
    re_path(r'^edit_form1/(?P<id>\d+)/', views.edit_form1),
    re_path(r'^edit_form2/(?P<id>\d+)/', views.edit_form2),
    re_path(r'^form1_db',views.form1_db),
    re_path(r'^form2_db',views.form2_db),
    re_path(r'^form1_xlsx', views.form1_xlsx),
    re_path(r'^form2_xlsx', views.form2_xlsx),
    re_path(r'^form1', views.form1),
    re_path(r'^form2', views.form2),
    re_path(r'^lists',views.lists),
    re_path(r'^all_forms', views.all_forms),
    re_path(r'^add_member', views.add_member),
    re_path(r'^add_item/(?P<type>\w+)/',views.add_item),
    re_path(r'^del_item/(?P<type>\w+)/(?P<id>\d+)/',views.del_item),
    path(r'', views.index),
]