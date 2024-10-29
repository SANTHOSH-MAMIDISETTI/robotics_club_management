from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User

def home(request):
    return render(request, 'core/home.html')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'users': users})

class LoginView(auth_views.LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True  # Redirect to home if already authenticated

    def form_valid(self, form):
        # Log the user in and redirect to home or user list
        user = form.get_user()
        login(self.request, user)
        return redirect('home')  # Change to 'user_list' if you want to redirect there

class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('logout_confirmation')  # Redirect to logout confirmation page

def logout_confirmation(request):
    return render(request, 'core/logout_confirmation.html')  # Ensure this template exists

# Optional: Handle unauthorized access
def unauthorized_access(request):
    return render(request, 'core/unauthorized_access.html')  # Ensure this template exists

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'core/profile.html', {'user': user})  # Ensure you create this template
