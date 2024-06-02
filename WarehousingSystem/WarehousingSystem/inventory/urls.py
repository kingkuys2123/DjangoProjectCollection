from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add_item/', views.add_item, name='add_item'),
    path("confirm_delete_item/<int:item_id>/", views.confirm_delete_item, name="confirm_delete_item"),
    path("confirm_delete_item/delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path("edit_item/<int:item_id>/", views.edit_item, name="edit_item"),
]
