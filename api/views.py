from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Serializers.UserSerializer import UserSerializer
from .Serializers.UserRegistrationSerializer import UserRegistrationSerializer
from .models.UserModel import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


#/api/
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
