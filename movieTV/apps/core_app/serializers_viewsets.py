"""
Django Rest Framework functions

Serializers and Viewsets for each model
"""
from rest_framework import serializers, viewsets, permissions
from core_app.models import User


# Serializers define the API representation..
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    full_name = serializers.SerializerMethodField(
        source="get_full_name")
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'is_superuser', 'full_name']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
