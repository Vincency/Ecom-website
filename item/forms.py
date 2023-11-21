from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

    widgets = {
        'category': forms.Select(attrs={
            'class': 'category-class',
        })
    }