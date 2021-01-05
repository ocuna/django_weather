from django.urls import path
# the "." means from the same folder as this file is in
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]
