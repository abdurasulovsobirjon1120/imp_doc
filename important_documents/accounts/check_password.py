from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Agar yangi foydalanuvchi yaratilayotgan bo'lsa
            self.set_password(self.password)  # Parolni hashlash
        super().save(*args, **kwargs)
