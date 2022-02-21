from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("", views.tag_index, name = "tag_index"),
    path("<int:tag_id>/", views.tag_detail, name="tag_detail")
]