from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='categories', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
