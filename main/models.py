import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('Shorts', 'shorts'),
        ('Ball', 'ball'),
        ('Shoes', 'shoes'),
        ('Shirts', 'shirts'),
        ('Hoodies', 'hoodies'),
        ('Socks', 'socks'),
    ]

    #name price desc thumb cat isfield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveBigIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
