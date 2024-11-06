from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]  # Faqat ro'yxatdan o'tish uchun

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Yangi token yaratish
        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "Registration successful", "token": token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]  # Autentifikatsiyani talab qilmaydi

    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number or not password:
            return Response({"message": "Phone number and password are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=phone_number, password=password)

        if user is not None:
            # Login muvaffaqiyatli bo'lsa, token qaytarish
            refresh = RefreshToken.for_user(user)  # Foydalanuvchi uchun refresh token yaratish
            return Response({
                "message": "Login successful",
                "access": str(refresh.access_token),  # Access token
                "refresh": str(refresh),  # Refresh token
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


User = get_user_model()

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]  # Bu yerda permission_classes ni AllowAny ga o'zgartirish

    def post(self, request):
        phone_number = request.data.get('phone_number')
        new_password = request.data.get('new_password')

        if not phone_number:
            raise ValidationError({"phone_number": ["This field is required."]})
        if not new_password:
            raise ValidationError({"new_password": ["This field is required."]})

        try:
            # Foydalanuvchini telefon raqamiga ko'ra olish
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({"detail": "User with this phone number does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Yangi parolni o'rnatish
        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)