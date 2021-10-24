from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from ...Serializers.UserRegistrationSerializer import UserRegistrationSerializer


# /api/register/
from ...models import User


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


# /api/users/banuser
@api_view(['POST'])
@permission_classes((IsAdminUser,))
def ban_user(request):
    user_to_ban = User.objects.get(id=request.data.get("user_id"))
    user_to_ban.is_active = False
    user_to_ban.save()
    return Response(str(user_to_ban.username) + " has been banned.")


# /api/users/unbanuser
@api_view(['POST'])
@permission_classes((IsAdminUser,))
def unban_user(request):
    user_to_unban = User.objects.get(id=request.data.get("user_id"))
    user_to_unban.is_active = True
    user_to_unban.save()
    return Response(str(user_to_unban.username) + " has been unbanned.")
