from django.urls import path

from . import views

app_name = "translation_app"
urlpatterns = [
    path("", views.index, name="index"),
]