from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.main_page_index, name = "main_page_index")
]