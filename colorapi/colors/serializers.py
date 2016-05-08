from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Color


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class Color(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('name', 'hexadecimal', 'red', 'green', 'blue')
