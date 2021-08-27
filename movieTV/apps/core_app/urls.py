from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from core_app import views, serializers_viewsets


app_name = 'core_app'

router = routers.DefaultRouter()
router.register(r'webusers', serializers_viewsets.WebUserViewSet)

urlpatterns = [
    url('^api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', views.homepage, name='home_page'),
    path('movies', views.movies, name='movies'),
]
