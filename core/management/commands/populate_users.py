from django.core.management.base import BaseCommand
from core.models import User, Role  # Import your custom User and Role models
from random import choice
from faker import Faker
import os

class Command(BaseCommand):
    help = 'Populate the database with dummy users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        roles = ['Admin', 'Staff', 'Mentor', 'Alumni', 'Mentee']
        groups = ['Mobile Robotics', 'Aerial Robotics', '3D Printer', '3D Design']

        # Create Role instances if they don't exist
        for role_name in roles:
            Role.objects.get_or_create(name=role_name)

        user_data = []  # List to store user information

        for _ in range(10):  # Adjust this number to create more or fewer users
            username = fake.user_name()
            email = fake.email()
            role_name = choice(roles)
            group_name = choice(groups)

            # Create user with password "test"
            user = User.objects.create_user(
                username=username,
                email=email,
                password='test'  # Setting password to "test"
            )

            # Get the Role instance
            role_instance = Role.objects.get(name=role_name)

            # Assign role to user
            user.role = role_instance
            user.save()

            # Save user data
            user_data.append({
                'username': username,
                'password': 'test',
                'role': role_name,
                'group': group_name
            })

            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username} with role {role_name}'))

        # Save user data to a file
        with open('user_data.txt', 'w') as file:
            for data in user_data:
                file.write(f"Username: {data['username']}, Password: {data['password']}, Role: {data['role']}, Group: {data['group']}\n")

        self.stdout.write(self.style.SUCCESS('User data has been saved to user_data.txt'))
