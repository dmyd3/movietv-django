"""
Django Rest Framework functions

Serializers and Viewsets for each model
"""
from rest_framework import serializers, viewsets
from .models import WebUser


# Serializers define the API representation.
class WebUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebUser
        fields = ['username', 'email', 'first_name', 'is_superuser']


# ViewSets define the view behavior.
class WebUserViewSet(viewsets.ModelViewSet):
    queryset = WebUser.objects.all()
    serializer_class = WebUserSerializer
