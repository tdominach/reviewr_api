from django.core.exceptions import ObjectDoesNotExist
from api.Views.POST.ReviewPostRequests import upvote_review
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from ...Serializers.ReviewSerializer import ReviewSerializer
from ...models import Review


# /api/reviews/
@api_view(['GET'])
@permission_classes((IsAdminUser,))
def show_all(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# /api/has_user_upvoted/{key}
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def has_user_upvoted(request, review_id):
    try:
        in_user_id = Token.objects.get(key=request.auth.key).user_id
        review = Review.objects.get(yelp_review_id=review_id)
        if review.has_user_upvoted(in_user_id):
            return Response("True")
        else:
            return Response("False")
    except ObjectDoesNotExist:
        return Response("False")


# /api/has_user_downvoted/{key}
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def has_user_downvoted(request, review_id):
    try:
        in_user_id = Token.objects.get(key=request.auth.key).user_id
        review = Review.objects.get(yelp_review_id=review_id)
        if review.has_user_downvoted(in_user_id):
            return Response("True")
        else:
            return Response("False")
    except ObjectDoesNotExist:
        return Response("False")


# /api/get_upvotes/{key}
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_upvotes(request, review_id):
    try:
        in_user_id = Token.objects.get(key=request.auth.key).user_id
        review = Review.objects.get(yelp_review_id=review_id)
        return Response(review.get_upvotes())
    except ObjectDoesNotExist:
        return Response(0)


# /api/get_downvotes/{key}
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_downvotes(request, review_id):
    try:
        in_user_id = Token.objects.get(key=request.auth.key).user_id
        review = Review.objects.get(yelp_review_id=review_id)
        return Response(review.get_downvotes())
    except ObjectDoesNotExist:
        return Response(0)
