from rest_framework import serializers
from . models import users
from django.contrib.auth.hashers import make_password

"""
A model serializer allows model instances to be 
converted into Python datatypes, so they can easily be 
rendered into JSON. 

https://www.django-rest-framework.org/api-guide/serializers/#serializers

"""


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = '__all__'  # '__all__' defines all fields within the model

    """
    The 'validate_password' function hashes the password before 
    it enters the database by utilizing REST frameworks field-level 
    validation.

    https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
       
    """

    def validate_pass_field(self, value):

        value = make_password(value)
        return value
