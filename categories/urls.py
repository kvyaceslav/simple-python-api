from django.urls import path
from categories.views import (index, show, add, update, delete)


urlpatterns = [
    path('', index),
    path('<int:id>', show),
    path('add', add),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
]
