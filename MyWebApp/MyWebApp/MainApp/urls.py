from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts_list/', views.posts_list, name='posts_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]