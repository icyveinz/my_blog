from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.my_first_view, name='my_view'),  # Example view URL
]