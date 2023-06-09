from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib import messages
from core.forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


def index_view(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()[0:5]
    return render(request, "core/index.html", context={"items": items, "categories": categories})


def contact_view(request):
    return render(request, "core/contact.html")


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("core:index")
        else:
            messages.error(request, "Invalid form submitted")
            return redirect("core:register")
    return render(request, "core/register.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username, password=password)
        except:
            messages.error(request, "User doesn't exist.")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("core:index")
    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect("core:index")
