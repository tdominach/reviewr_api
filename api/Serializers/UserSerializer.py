from rest_framework import serializers
from ..Models.UserModel import users
from django.contrib.auth.hashers import make_password
from ..VerificationServices import UserVerificationService

"""
A model serializer allows model instances to be 
converted into Python datatypes, so they can easily be 
rendered into JSON. 

Link to Documentation:
https://www.django-rest-framework.org/api-guide/serializers/#serializers

"""


class userSerializer(serializers.ModelSerializer):
    # validate_<ELEMENT>(self, <ELEMENT>):
    # automatically called, must return <ELEMENT> if it passed, else throw an error like:
    # raise serializers.ValidationError('Rating has to be between 1 and 10.')

    class Meta:
        model = users
        fields = '__all__'  # '__all__' defines all fields within the model
        app_label = "api" # This is needed to identify what app this model belongs to.

    def validate_password(self, password):
        print("validate password was called") # TODO remove this after seeing it actually is called.
        if UserVerificationService.verifyPassword(password):
            return make_password(password)
        else:
            raise serializers.ValidationError('Password failed verification.')

    def validate_username(self, username):
        # TODO make this check for duplicates.
        if UserVerificationService.verifyUsername(username):
            return username
        else:
            raise serializers.ValidationError('Username failed verification.')

    def validate_email(self, email):
        # TODO make this check for duplicates.
        if UserVerificationService.verifyEmail(email):
            return email
        else:
            raise serializers.ValidationError('Email failed verification.')