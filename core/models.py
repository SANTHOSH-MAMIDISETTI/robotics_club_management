# core/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='mentored_groups')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='member_groups', blank=True)

    class Meta:
        permissions = [
            ('view_own_groups', 'Can view own groups'),
        ]

    def __str__(self):
        return f"{self.name} (Mentor: {self.mentor.username if self.mentor else 'None'})"

    def clean(self):
        # Ensure that the mentor is unique to this group
        if self.mentor and Group.objects.exclude(id=self.id).filter(mentor=self.mentor).exists():
            raise ValidationError(f"{self.mentor.username} is already a mentor for another group.")

        # Ensure that each member belongs to only one group
        for member in self.members.all():
            if Group.objects.exclude(id=self.id).filter(members=member).exists():
                raise ValidationError(f"{member.username} is already a member of another group.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean to validate before saving
        super().save(*args, **kwargs)
