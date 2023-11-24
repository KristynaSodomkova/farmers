from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterUserView, name="register_user"),
    path('users/', views.UserDetailView, name="users_list"),
    path('users/<user_id>', views.UserDetailView, name="user_detail"),
]
