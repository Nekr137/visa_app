from django.contrib import admin
from django.urls import path,re_path

from app import views

urlpatterns = [
    #path('edit/<int:id>/', views.edit),
    re_path(r'^edit_form2/(?P<id>\d+)/', views.edit_form2),
    re_path(r'^rewrite_dates_in_form', views.rewrite_dates_in_form),
    re_path(r'^form2_html', views.form2_html),
    re_path(r'^form2_db/(?P<sort_item>\w+)/(?P<reverse>\w+)/',views.form2_db),
    re_path(r'^form2_xlsx', views.form2_xlsx),
    re_path(r'^render_pdf_view',views.render_pdf_view),
    re_path(r'^save_form/(?P<visa_type>\w+)/', views.save_form),
    re_path(r'^form/(?P<visa_type>\w+)/', views.form),
    re_path(r'^lists',views.lists),
    re_path(r'^add_member', views.add_member),
    re_path(r'^add_item/(?P<type>\w+)/',views.add_item),
    re_path(r'^del_item/(?P<type>\w+)/(?P<id>\d+)/',views.del_item),
    re_path(r'^default/(?P<type>\w+)/(?P<id>\d+)/',views.default),
    re_path(r'^rewrite_visanumber',views.rewrite_visanumber),
    re_path(r'^increment_visanumber',views.increment_visanumber),
    re_path(r'^statistic',views.statistic),
    path(r'', views.index),
    re_path(r'^html2pdf/(?P<id>\w+)/',views.html2pdf),
]