from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("", views.index, name="ppv_index"),
    path("<int:ppv_id>",views.detail, name = "ppv_detail"),
    path("<int:ppv_id>/<int:title_id>",views.title_detail, name = "ppv_title_detail"),
]