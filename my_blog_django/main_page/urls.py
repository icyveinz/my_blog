from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_render, name='main_page'),
]