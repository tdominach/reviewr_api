from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ...Serializers.UpdateUserSerializers import UpdateUsernameSerializer
from ...Serializers.UpdateUserSerializers import UpdateFirstNameSerializer
from ...Serializers.UpdateUserSerializers import UpdateLastNameSerializer
from ...Serializers.UpdateUserSerializers import UpdateEmailSerializer

# /api/users/update/username/
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_username(request):
    user = request.user
    serializer = UpdateUsernameSerializer(user, data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data["success"] = "Username successfully updated"
        return Response(data=data)

    return Response(serializer.errors)

# /api/users/update/firstname/
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_first_name(request):
    user = request.user
    serializer = UpdateFirstNameSerializer(user, data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data["success"] = "First name successfully updated"
        return Response(data=data)

    return Response(serializer.errors)

# /api/users/update/lastname/
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_last_name(request):
    user = request.user
    serializer = UpdateLastNameSerializer(user, data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data["success"] = "Last name successfully updated"
        return Response(data=data)

    return Response(serializer.errors)

# /api/users/update/email/
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_email(request):
    user = request.user
    serializer = UpdateEmailSerializer(user, data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data["success"] = "Email successfully updated"
        return Response(data=data)

    return Response(serializer.errors)
