from item.models import Item
from django import forms


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "price", "description", "image",)

        widgets = {
            "category": forms.Select(attrs={
                "class": "new-item-field"
            }),
            "name": forms.TextInput(attrs={
                "class": "new-item-field"
            }),
            "price": forms.TextInput(attrs={
                "class": "new-item-field"
            }),
            "description": forms.Textarea(attrs={
                "class": "new-item-field"
            }),
            "image": forms.FileInput(attrs={
                "class": "new-item-field"
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "price", "description", "image", "is_sold",)

        widgets = {
            "category": forms.Select(attrs={
                "class": "new-item-field"
            }),
            "name": forms.TextInput(attrs={
                "class": "new-item-field"
            }),
            "price": forms.TextInput(attrs={
                "class": "new-item-field"
            }),
            "description": forms.Textarea(attrs={
                "class": "new-item-field"
            }),
            "image": forms.FileInput(attrs={
                "class": "new-item-field"
            }),
            "is_sold": forms.CheckboxInput(attrs={
                "class": "new-item-field"
            })
        }
