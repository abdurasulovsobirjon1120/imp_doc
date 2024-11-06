from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)  # Token maydonini o'qish uchun

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}  # Parol faqat yozish uchun

    def create(self, validated_data):
        # Foydalanuvchini yaratish
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        # Foydalanuvchi yaratilgandan keyin unga token yaratish
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        # Tokenni olish
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=128, write_only=True)

class ResetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    new_password = serializers.CharField(max_length=128, write_only=True)
