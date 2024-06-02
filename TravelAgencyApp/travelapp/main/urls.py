from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('package_details/<int:package_id>/', views.package_details, name='package_details'),
    path('package_details/add_package_review/<int:package_id>/', views.add_package_review, name='add_package_review'),
]