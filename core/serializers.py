from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    user_type = serializers.CharField(read_only=True)
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password', 'placeholder': 'Confirm Password'})
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username','password','password2', 'email', 'first_name', 'last_name', 'phone', 'user_type']
    
    def validate(self, attrs):
        attrs = dict(attrs)
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password == password2:
            return super().validate(attrs)
        else:
            raise serializers.ValidationError({"error" : "password doesn't match"})
       
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