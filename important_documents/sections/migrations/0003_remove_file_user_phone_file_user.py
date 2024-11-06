# Generated by Django 5.1.2 on 2024-11-01 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_alter_section_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='user_phone',
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
