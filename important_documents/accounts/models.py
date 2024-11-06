from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")
        if not phone_number:
            raise ValueError("Phone number required")

        # Email va telefon raqamini normalize qilish
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Parolni hash qilish
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        """
        Superuser yaratish uchun metod
        """
        # Superuser uchun zarur bo'lgan maydonlar
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True, blank=True, default="Unknown")
    last_name = models.CharField(max_length=30, null=True, blank=True, default="Unknown")
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=14, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'  # Telefon raqamini username sifatida belgilash
    REQUIRED_FIELDS = ['email']  # Superuser yaratish uchun email zarur

    def __str__(self):
        return self.email
