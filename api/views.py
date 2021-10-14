from rest_framework.response import Response
from rest_framework.decorators import api_view
from reviewr_api.api.Serializers.UserSerializer import userSerializer
from .Models.UserModel import users

# Create your views here.

#/api/
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User List': '/users/',
        'User Details': '/users/<int:id>',
        'Register': '/register/',
    }
    return Response(api_urls)


# /api/users/
@api_view(['GET'])
def ShowAll(request):
    Users = users.objects.all()
    serializer = userSerializer(Users, many=True)
    return Response(serializer.data)


# /api/users/{id}
@api_view(['GET'])
def viewUser(request, pk):
    User = users.objects.get(id=pk)
    serializer = userSerializer(User, many=False)
    return Response(serializer.data)


# /api/register/
@api_view(['POST'])
def registerUser(request):
    serializer = userSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
