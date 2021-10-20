from rest_framework import serializers
from ..models.UserModel import User

"""
A model serializer allows model instances to be 
converted into Python datatypes, so they can easily be 
rendered into JSON. 

Link to Documentation:
https://www.django-rest-framework.org/api-guide/serializers/#serializers

"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # '__all__' defines all fields within the model
        app_label = "api" # This is needed to identify what app this model belongs to.