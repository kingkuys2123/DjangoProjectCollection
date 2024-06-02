from django.urls import path
from . import views

urlpatterns = [
    path('', views.gift_list, name='gift_list'),
    path('gift/<int:pk>/', views.gift_detail, name='gift_detail'),
]