from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

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

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exists.")
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')

        if pw != pw2:
            raise serializers.ValidationError("Password must match.")
        return data

    def create(self, validated_data):
        user_obj = User(
            username=validated_data.get('name'),
            email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = True
        user_obj.is_staff = True
        user_obj.save()
        return user_obj