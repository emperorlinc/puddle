from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item

# Create your views here.


@login_required(login_url="core:login")
def my_item(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, "dashboard/my_item.html", context={"items": items})
