from django.urls import path
from . import views

app_name = "core"
# Create your urlpatterns here.
urlpatterns = [
    path("", views.index_view, name="index"),
    path("contact/", views.contact_view, name="contact"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
]
