from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')

        if pw != pw2:
            raise serializers.ValidationError("Password must match.")
        return data

    def create(self, validated_data):
        user_obj = User(
            name=validated_data.get('name'),
            email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = True
        user_obj.is_staff = True
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'name',  'is_active', 'is_staff', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff', 'auth_token')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class EmptySerializer(serializers.Serializer):
    pass