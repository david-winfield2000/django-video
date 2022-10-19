from urllib.parse import urlunparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]