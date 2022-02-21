from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("", views.index, name="title_index"),
    path("<int:title_id>/", views.title_detail, name="title_detail"),
    path("<int:title_id>/sorted_name", views.title_detail_name, name="title_detail_name"),
    path("<int:title_id>/sorted_name_down", views.title_detail_name_down, name="title_detail_name_down"),
    path("<int:title_id>/sorted_titles", views.title_detail_titles, name="title_detail_titles"),
    path("<int:title_id>/sorted_titles_down", views.title_detail_titles_down, name="title_detail_titles_down"),
    path("<int:title_id>/sorted_days_down", views.title_detail_days_down, name="title_detail_days_down"),
]
