from rest_framework import serializers
from ..models.ReviewModel import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'
        app_label = "api"
