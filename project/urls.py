from django.contrib import admin
from django.urls import path
from products.views import (
    index as product_index,
    show as product_show,
    add as product_add,
    update as product_update,
    delete as product_delete,
)
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/product/', product_index),
    path('api/product/<int:id>', product_show),
    path('api/product/add', product_add),
    path('api/product/update/<int:id>', product_update),
    path('api/product/delete/<int:id>', product_delete),
]
