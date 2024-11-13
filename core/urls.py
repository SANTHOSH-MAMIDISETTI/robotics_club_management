# core/urls.py
from django.urls import path
from .views import (
    home, user_list, LoginView, LogoutView, logout_confirmation, profile,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    GroupListView, GroupCreateView, GroupUpdateView, GroupDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout_confirmation/', logout_confirmation, name='logout_confirmation'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('group/create/', GroupCreateView.as_view(), name='group_create'),
    path('group/<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('group/<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
]