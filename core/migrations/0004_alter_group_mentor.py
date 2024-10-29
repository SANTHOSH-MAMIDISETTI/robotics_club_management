# Generated by Django 5.1.2 on 2024-10-29 06:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_group_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mentor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentored_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
