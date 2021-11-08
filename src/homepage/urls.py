"""Defines urls"""
from django.urls import path

from . import views

# The namespace of the apps' URLconf
app_name = "homepage"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.index, name="index"),
]
