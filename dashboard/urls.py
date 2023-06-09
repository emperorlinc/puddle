from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("my_items/", views.my_item, name="my-item"),
]
