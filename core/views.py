from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  # Import to get custom user model
from .models import Group  # Keep Group as is

User = get_user_model()  # Use this dynamically to refer to custom user model

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

# User CRUD Views
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import RegistrationForm

class UserListView(ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'role']
    template_name = 'core/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'core/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

# Group CRUD Views
class GroupListView(ListView):
    model = Group
    template_name = 'core/group_list.html'
    context_object_name = 'groups'

class GroupCreateView(CreateView):
    model = Group
    fields = ['name', 'mentor', 'members']
    template_name = 'core/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name', 'mentor', 'members']
    template_name = 'core/group_form.html'
    success_url = reverse_lazy('group_list')

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'core/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')
