from rest_framework import serializers
from ..models.UserModel import User
from ..VerificationServices import UserVerificationService

# This file contains all the serializers that are used to update an attribute of the users profile.
# In order to keep the 'Serializers' folder from getting too crowded each update serializer is written here.


class UpdateUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        app_label = "api"

    def validate_username(self, username):
        if UserVerificationService.verifyUsername(username):
            if not User.objects.filter(username=username).exists():
                return username
            else:
                raise serializers.ValidationError(
                    'Username already exists on another account.')
        else:
            raise serializers.ValidationError('Username failed verification.')


class UpdateFirstNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']
        app_label = "api"


class UpdateLastNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name']
        app_label = "api"


# TO-DO Add serializer for updating a users profile picture.
