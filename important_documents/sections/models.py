from django.db import models
from django.conf import settings

class Section(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.user})"

class File(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='documents/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=20)
    file_size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.file_name
