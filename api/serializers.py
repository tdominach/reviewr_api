from rest_framework import serializers
from . models import users
from django.contrib.auth.hashers import make_password

"""
A model serializer allows model instances to be 
converted into Python datatypes, so they can easily be 
rendered into JSON. 

Link to Documentation:
https://www.django-rest-framework.org/api-guide/serializers/#serializers

"""


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = '__all__'  # '__all__' defines all fields within the model

    """
    The 'validate_password' function hashes the password before 
    it enters the database by utilizing REST frameworks field-level 
    validation. This type of validation can be used to add password
    username requirements.

    Link to Documentation:
    https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
       
    """

    def validate_password(self, value):

        # make_password() function hashes the password
        value = make_password(value)
        return value
