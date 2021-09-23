from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from core_app import views, serializers_viewsets


app_name = 'core_app'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', serializers_viewsets.UserViewSet)

urlpatterns = [
    url('api/', include(router.urls)),
    path('accounts/singup', views.signup, name='signup'),

    path('', views.homepage, name='home_page'),
    path('movies/', views.movies, name='movies'),
    path('movies/<str:tmdb_id>', views.get_movie_info, name='individual_movie'),
    path('profile/', views.my_profile, name='my_profile'),
    path('users/<str:user_id>', views.user_profile, name='user_profile'),

    path('ajax/watch_movie', views.watch_movie, name='watch_movie'),
    path('ajax/fav_movie', views.fav_movie, name='fav_movie'),
]
