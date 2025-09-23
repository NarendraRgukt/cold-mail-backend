from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # uses Django session login
            csrf_token = get_token(request)  # generate CSRF token for client
            return Response({
                "message": "Login successful",
                "csrf_token": csrf_token
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)