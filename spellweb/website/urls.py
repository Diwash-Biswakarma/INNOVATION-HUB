from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [

    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('apply/', views.apply, name='apply'),
    path('contact/', views.contact, name='contact'),
    path('info/', views.info, name='info'),
    path('media/', views.media, name='media'),
    path('new_apply/', views.new_apply, name='new_apply')

]