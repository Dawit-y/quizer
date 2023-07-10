from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    user_type = serializers.CharField(read_only=True)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name', 'phone', 'user_type']
    
    def create(self, validated_data):
        return super().create(validated_data)

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']

