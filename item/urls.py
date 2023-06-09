from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("<int:pk>/", views.detail_view, name="detail"),
    path("new_item/", views.new_item_view, name="new-item"),
    path("<int:pk>/delete/", views.delete_item, name="delete"),
    path("<int:pk>/edit", views.edit_item_view, name="edit"),
]
