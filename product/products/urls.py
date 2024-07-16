# your_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.inquiry_view, name="contact"),
]
