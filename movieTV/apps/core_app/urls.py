from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from core_app import views, serializers_viewsets


app_name = 'core_app'

router = routers.DefaultRouter()
router.register(r'users', serializers_viewsets.UserViewSet)

urlpatterns = [
    url('^api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/singup', views.signup, name='signup'),

    path('', views.homepage, name='home_page'),
    path('movies/', views.movies, name='movies'),
    path('movies/<str:tmdb_id>', views.get_movie_info, name='individual_movie'),
]
