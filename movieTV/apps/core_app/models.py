from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.postgres.fields import ArrayField

import re
from django.utils.translation import gettext_lazy as _


# validators=[validators.RegexValidator(re.compile(r'^[\w.@+-]+$'),
# 'Nome de usuario invalido, só pode conter @/./+/-/','invalid')] #Username-CharField

class User (AbstractUser):
    '''
        User of the app, inherits essential fields from AbstractUser

        Important Fields: username, email, password, first_name, last_name
        Important functions: get_full_name
    '''
    movies_watched = ArrayField(
        models.JSONField(name=_('Movies')),
        verbose_name=_('Movies Watched'),
        help_text=_('Movies that the user have watched'),
        blank= True, default=list
    )

    movies_favorite = ArrayField(
        models.JSONField(name=_('Movies')),
        verbose_name=_('Favorite Movies'),
        help_text=_('Movies that the user have as favorites'),
        blank= True, default=list
    )

    series_watched = ArrayField(
        models.JSONField(name=_('TV Shows')),
        verbose_name=_('Shows Watched'),
        help_text=_('Shows that the user have watched'),
        blank= True, default=list
    )

    # overwrite
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=_('groups'),
    #     blank=True,
    #     help_text=_(
    #         'The groups this user belongs to. A user will get all permissions '
    #         'granted to each of their groups.'
    #     ),
    #     related_name="webuser_set",
    #     related_query_name="webuser",
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     help_text=_('Specific permissions for this user.'),
    #     related_name="webuser_set",
    #     related_query_name="webuser",
    # )

    # REQUIRED_FIELDS = ['email']
    # JSON objects format: { original title: "Loki", release_year: 2015, tmdb_ID: 9999 }
    # to be added: favorite movies, favorite series, avatar picture

class FriendList (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)