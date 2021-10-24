from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from ...Serializers.ReviewSerializer import ReviewSerializer
from ...models import Review


# /api/reviews/
@api_view(['GET'])
@permission_classes((IsAdminUser,))
def show_all(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
