# Generated by Django 5.1.2 on 2024-11-01 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_remove_file_user_phone_file_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='size',
            new_name='file_size',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='file_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to=settings.AUTH_USER_MODEL),
        ),
    ]