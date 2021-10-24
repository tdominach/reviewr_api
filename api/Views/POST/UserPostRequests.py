from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from ...Serializers.UserRegistrationSerializer import UserRegistrationSerializer


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
