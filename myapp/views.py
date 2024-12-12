from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MyUser
from .Serializers import MyUserProfileSerializer

# Create your views here.
@api_view(['GET'])
def get_user_profile_data(request, pk):
    try:
        try:
         user = MyUser.objects.get(username=pk)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MyUserProfileSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response(('error:error getting user profile data'))