from django.urls import path
from .views import home, user_list, LoginView, LogoutView, logout_confirmation, profile

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('user_list/', user_list, name='user_list'),  # User list page
    path('login/', LoginView.as_view(), name='login'),  # Login page
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL
    path('logout_confirmation/', logout_confirmation, name='logout_confirmation'),  # Logout confirmation page
    path('profile/<int:user_id>/', profile, name='profile'),  # User profile page
]
