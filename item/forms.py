from django import forms
    
from .models import Item


class NewItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'category-class',
            }),
        
            'name': forms.TextInput(attrs={
                'class': 'category-class',
            }),

            'description': forms.Textarea(attrs={
                'class': 'category-class',
            }),
       
            'price': forms.TextInput(attrs={
                'class': 'category-class',
            }),

            'image': forms.TextInput(attrs={
                'class': 'category-class',
            })
        }
