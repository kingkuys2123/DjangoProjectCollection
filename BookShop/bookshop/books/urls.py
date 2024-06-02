from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse_books/', views.browse_books, name='browse_books'),
]