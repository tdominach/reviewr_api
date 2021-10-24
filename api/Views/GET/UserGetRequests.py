from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ...Serializers.UserSerializer import UserSerializer
from ...models import User


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
