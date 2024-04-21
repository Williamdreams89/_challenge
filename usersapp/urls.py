from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
]