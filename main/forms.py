from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags # Assignment 6

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'stock', 'rating']

    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)
    
    def clean_category(self):
        category = self.cleaned_data['category']
        return strip_tags(category)