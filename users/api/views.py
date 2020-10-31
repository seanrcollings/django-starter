from ..models import User
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerialzer

### API ###
class UserViewSet(viewsets.ModelViewSet):
    """API Endpoint to view or edit users"""

    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerialzer
    permission_classes = [permissions.IsAuthenticated]


# class ListUsers(views.APIView):
#     def get(self, request, format=None):
#         breakpoint()


# @api_view(["GET"])
# def test_view(request):
#     print("hi there")
#     breakpoint()
#     return Response({"message": "hello there"})
