from django.urls import path
from authentication.views import RegisterView
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
