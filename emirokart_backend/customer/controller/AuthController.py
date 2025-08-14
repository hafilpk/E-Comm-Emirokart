from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"message": "Both username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            return Response({
                "refresh": str(refresh),
                "access": str(access),
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        return Response(
            {"message": "Please use POST method to login"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
