from django.contrib.auth.models import User, Group
from .model import Color
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ColorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for view and edit users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for view and edit Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by('name')
    serializer_class = ColorSerializer
