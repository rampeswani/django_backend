from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .services import register_user, login_user, get_user_info


class RegisterView(APIView):
    def post(self, request):
        try:
            result = register_user(request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response(ve.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Unexpected error", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        try:
            result = login_user(request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response(ve.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Unexpected error", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    try:
        result = get_user_info(request.user)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Failed to retrieve user information", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
