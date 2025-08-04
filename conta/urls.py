from django.urls import path
from conta.views import login, register

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
]