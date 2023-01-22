from django.urls import path

from . import views
# app_name = "show"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("random/", views.randomPage, name="randomPage"),
    path("delete/", views.delete, name="delete")
]
