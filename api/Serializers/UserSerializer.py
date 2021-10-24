from rest_framework import serializers
from ..models.UserModel import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        app_label = "api"
