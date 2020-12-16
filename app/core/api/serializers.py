from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
from rest_framework.reverse import reverse as api_reverse

from core.models import Palestrante, Palestra

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
        payload = jwt_payload_handler(user=obj)
        token = jwt_encode_handler(payload)
        return token


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


class PalestraDataSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Palestrante
        fields = [
            'uri',
            'nome',
            'titulo',

        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-core:lectures_detail', kwargs={"pk": obj.pk}, request=request)


class PalestranteSerializer(serializers.ModelSerializer):

    uri = serializers.SerializerMethodField(read_only=True)
    palestra = PalestraDataSerializer(read_only=True)

    class Meta:
        model = Palestrante
        fields = [
            'id',
            'uri',
            'nome',
            'bio',
            'palestra',
        ]

        read_only_fields = ['id', 'uri']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-core:speaker', kwargs={"pk": obj.pk}, request=request)


class PalestranteDetailSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=120)
    bio = serializers.CharField(max_length=2000, allow_null=True)

    def create(self, validated_data):
        return Palestrante.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance


class PalestranteNomeSerializer(serializers.ModelSerializer):

    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Palestrante
        fields = [
            'nome',
            'uri',
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-core:speaker', kwargs={"pk": obj.pk}, request=request)


class PalestraSerializer(serializers.ModelSerializer):
    """ Speaker"""
    uri = serializers.SerializerMethodField(read_only=True)
    nome = PalestranteNomeSerializer(required=False, read_only=True)

    class Meta:
        model = Palestra
        fields = [
            'id',
            'uri',
            'titulo',
            'descricao',
            'data',
            'nome',
        ]

        read_only_fields = ['id', 'data']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-core:lectures_detail', kwargs={"pk": obj.pk}, request=request)


class PalestraDetailSerializer(serializers.Serializer):
    """ Lecture """
    palestrante = serializers.CharField(max_length=255)
    titulo = serializers.CharField(max_length=255)
    descricao = serializers.CharField(max_length=2000, allow_null=True)
    data = serializers.DateTimeField()

    def create(self, validated_data):
        return Palestrante.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.palestrante = validated_data.get('palestrante', instance.palestrante)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance