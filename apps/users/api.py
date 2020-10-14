from rest_framework.response import Response
from apps.serializers.serialiazerUser import SerialiazerUser
from rest_framwork.views import APIView
from rest_framework import status

class UserAPI(APIView):
    def post(self, request):
        serializer = SerialiazerUser(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
