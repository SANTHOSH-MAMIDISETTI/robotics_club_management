#  core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.contrib.auth import get_user_model
from .models import Group
from .forms import RegistrationForm

User = get_user_model()  # Dynamically refer to custom user model

def home(request):
    return render(request, 'core/home.html')

# Protect the user list with login_required
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'users': users})

# Login view with redirection for already authenticated users
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
    return render(request, 'core/logout_confirmation.html')

# Optional: Handle unauthorized access
def unauthorized_access(request):
    return render(request, 'core/unauthorized_access.html')

# Profile view: Only logged-in users can access
@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'core/profile.html', {'user': user})

# User CRUD Views

# User List View (ensure it's protected by login)
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'
    login_url = '/login/'  # Specify custom login URL if needed

class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Ensure password is hashed
        user.save()
        login(self.request, user)  # Log the user in after registration
        return redirect(self.success_url)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'role']
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')
    login_url = '/login/'  # Ensure only logged-in users can access

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'core/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    login_url = '/login/'  # Ensure only logged-in users can access

# Group CRUD Views

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'core/group_list.html'
    context_object_name = 'groups'
    login_url = '/login/'  # Ensure only logged-in users can access

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'mentor', 'members']
    template_name = 'core/group_form.html'
    success_url = reverse_lazy('group_list')
    login_url = '/login/'  # Ensure only logged-in users can access

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name', 'mentor', 'members']
    template_name = 'core/group_form.html'
    success_url = reverse_lazy('group_list')
    login_url = '/login/'  # Ensure only logged-in users can access

class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'core/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')
    login_url = '/login/'  # Ensure only logged-in users can access
