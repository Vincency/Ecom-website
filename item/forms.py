from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = '__all__'