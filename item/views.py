from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.forms import EditItemForm, NewItemForm
from .models import Category, Item
from django.db.models import Q

# Create your views here.


def items(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get("query", "")
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "item/browse.html", context={
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id)
    })


def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, "item/detail.html", context={"item": item, "related_item": related_item})


@login_required(login_url="core:login")
def new_item_view(request):
    form = NewItemForm()
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    return render(request, "item/new_item.html", context={"form": form})


@login_required(login_url="core:login")
def edit_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    form = EditItemForm(instance=item)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=pk)
    return render(request, "item/edit_item.html", context={"form": form})


@login_required(login_url="core:login")
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:my-item")
