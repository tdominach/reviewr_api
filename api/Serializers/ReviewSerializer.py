from rest_framework import serializers
from ..models.ReviewModel import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        app_label = "api"
