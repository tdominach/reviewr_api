from rest_framework import serializers

from ..models.ReviewModel import Review


class ReviewRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["yelp_review_id"]
        app_label = "api"

    def save(self):
        review = Review(
            yelp_review_id=self.validated_data["yelp_review_id"],
            upvote=0,
            downvote=0
        )
        review.save()
        return review