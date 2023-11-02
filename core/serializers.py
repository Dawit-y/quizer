from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    user_type = serializers.CharField(read_only=True)
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username','password','password2', 'email', 'first_name', 'last_name', 'phone', 'user_type']
    
    def create(self, validated_data):
        print( "validated_data", validated_data)
        return super().create(validated_data)

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_name'] = user.username
        # ...

        return token