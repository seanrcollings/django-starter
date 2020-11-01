from ..models import User
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API Endpoint to view or edit users"""

    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        # entry point from the route
        return super().create(request, *args, **kwargs)

    def perform_create(self, request, *args, **kwargs):
        # calls serializer.save
        # used for post-validation data addition / changes
        return super().perform_create(request, *args, **kwargs)