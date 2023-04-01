from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    owner = models.ForeignKey(
        'auth.User', related_name='products', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
