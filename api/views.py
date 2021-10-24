from rest_framework.response import Response
from rest_framework.decorators import api_view

from .Serializers.ReviewRegistrationSerializer import ReviewRegistrationSerializer
from .Serializers.UserSerializer import UserSerializer
from .Serializers.UserRegistrationSerializer import UserRegistrationSerializer
from .models import Review
from .models.UserModel import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


# /api/
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'User List': '/users/',
        'User Details': '/users/<int:id>',
        'Register': '/register/',
    }
    return Response(api_urls)


# /api/users/
@api_view(['GET'])
@permission_classes((IsAdminUser,))
def show_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# /api/users/{id}
@api_view(['GET'])
def view_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# /api/users/self
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_own_user(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# /api/register/
@api_view(['POST'])
@permission_classes((AllowAny,))
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)


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


# /api/review/upvote
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def upvote_review(request):
    in_user_id = Token.objects.get(key=request.auth.key).user_id
    review = Review.objects.get(id=request.data.get('review_id'))
    if not review.has_user_upvoted(in_user_id):
        review.upvote_review(in_user_id)
        review.save()
        return Response("Upvoted post.")
    else:
        review.upvote_review(in_user_id)
        review.save()
        return Response("Removing upvote from post.")


# /api/review/downvote
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def downvote_review(request):
    in_user_id = Token.objects.get(key=request.auth.key).user_id
    review = Review.objects.get(id=request.data.get('review_id'))
    if not review.has_user_downvoted(in_user_id):
        review.downvote_review(in_user_id)
        review.save()
        return Response("Downvoted post.")
    else:
        review.downvote_review(in_user_id)
        review.save()
        return Response("Removing downvote from post.")