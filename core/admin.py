# core/admin.py
from django.contrib import admin
from .models import User, Role, Group

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor')
    search_fields = ('name',)
    list_filter = ('mentor',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # If the user is not a superuser, filter groups based on the user's membership
        return qs.filter(members=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.members.add(request.user)  # Automatically add the user as a member if they are creating a new group
        super().save_model(request, obj, form, change)
