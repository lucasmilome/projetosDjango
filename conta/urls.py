from django.urls import path
from conta.views import login, register, logout

urlpatterns = [
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
]
