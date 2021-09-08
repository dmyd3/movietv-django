"""
Django Rest Framework functions

Serializers and Viewsets for each model
"""
from rest_framework import serializers, viewsets
from core_app.models import User


# Serializers define the API representation..
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'is_superuser']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
