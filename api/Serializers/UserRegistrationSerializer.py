from rest_framework import serializers

from ..models.UserModel import User
from django.contrib.auth.hashers import make_password, check_password
from ..VerificationServices import UserVerificationService


class UserRegistrationSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'passwordConfirm']
        app_label = "api" # This is needed to identify what app this model belongs to.
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        passwordConfirm = self.validated_data['passwordConfirm']

        if check_password(password, passwordConfirm):
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user

    def validate_password(self, password):
        if UserVerificationService.verifyPassword(password):
            return make_password(password)
        else:
            raise serializers.ValidationError('Password failed verification.')

    def validate_username(self, username):
        if UserVerificationService.verifyUsername(username):
            if not User.objects.filter(username=username).exists():
                return username
            else:
                raise serializers.ValidationError('Username already exists on another account.')
        else:
            raise serializers.ValidationError('Username failed verification.')

    def validate_email(self, email):
        if UserVerificationService.verifyEmail(email):
            if not User.objects.filter(email=email).exists():
                return email
            else:
                raise serializers.ValidationError('Email already exists on another account.')
        else:
            raise serializers.ValidationError('Email failed verification.')