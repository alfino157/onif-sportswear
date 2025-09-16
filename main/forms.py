from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "description", "category", "thumbnail", "price", "stock", "is_featured"]