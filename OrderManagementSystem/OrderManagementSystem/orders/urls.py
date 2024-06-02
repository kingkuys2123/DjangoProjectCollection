from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('add_order/', views.add_order, name='add_order'),
    path("confirm_delete_order/<int:order_id>/", views.confirm_delete_order, name="confirm_delete_order"),
    path("confirm_delete_order/delete/<int:order_id>/", views.delete_order, name="delete_order"),
    path("customer_orders/<int:customer_id>/", views.customer_orders, name="customer_orders"),
    path("product_orders/<int:product_id>/", views.product_orders, name="product_orders"),
]
