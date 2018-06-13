from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.articles_list)
]
