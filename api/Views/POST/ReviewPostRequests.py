from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from ...Serializers.ReviewRegistrationSerializer import ReviewRegistrationSerializer
from ...models import Review


# /api/review/create
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def register_review(request):
    if request.method == 'POST':
        serializer = ReviewRegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            review = serializer.save()
            data['response'] = "successfully registered a new review."
        else:
            data = serializer.errors

        return Response(data)


# /api/reviews/upvote
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def upvote_review(request):
    in_user_id = Token.objects.get(key=request.auth.key).user_id
    try:
        review = Review.objects.get(yelp_review_id=request.data.get('yelp_review_id'))
        if not review.has_user_upvoted(in_user_id):
            review.upvote_review(in_user_id)
            review.save()
            return Response("Upvoted post.")
        else:
            review.upvote_review(in_user_id)
            review.save()
            return Response("Removing upvote from post.")
    except ObjectDoesNotExist:
        serializer = ReviewRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            review.upvote_review(in_user_id)
            review.save()
            return Response("Upvoted post.")
        else:
            return Response("Serializer not valid")


# /api/review/downvote
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def downvote_review(request):
    in_user_id = Token.objects.get(key=request.auth.key).user_id
    try:
        review = Review.objects.get(yelp_review_id=request.data.get('yelp_review_id'))
        if not review.has_user_downvoted(in_user_id):
            review.downvote_review(in_user_id)
            review.save()
            return Response("Downvoted post.")
        else:
            review.downvote_review(in_user_id)
            review.save()
            return Response("Removing downvote from post.")
    except ObjectDoesNotExist:
        serializer = ReviewRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            review.downvote_review(in_user_id)
            review.save()
            return Response("Downvoted post.")
        else:
            return Response("Serializer not valid")

# /api/review/delete
@api_view(["POST"])
@permission_classes((IsAdminUser,))
def delete_review(request):
    review = Review.objects.get(id=request.data.get('review_id'))
    review.delete()
    return Response("Deleted review")