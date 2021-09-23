from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from django.conf import settings

import re, os


# validators=[validators.RegexValidator(re.compile(r'^[\w.@+-]+$'),
# 'Nome de usuario invalido, só pode conter @/./+/-/','invalid')] #Username-CharField


class UsedMovie (models.Model):
    '''
        Used movies by this system users,
        only basic information
    '''
    original_title = models.CharField(
        verbose_name=_('Original Title'),
        max_length=300,
        blank=False, null=False
    )
    release_year = models.PositiveIntegerField(
        verbose_name=_('Release Year'),
        validators=[MinValueValidator(1800)],
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('Duration'),
    )

    tmdb_id = models.CharField(
        verbose_name=_('TMDB ID'),
        max_length=30,
        help_text=_('ID in The Movie DataBase'),
        unique=True,
        blank=False, null=False
    )

    def __str__(self):
        return self.original_title +" - "+ str(self.release_year)

    class Meta:
        verbose_name = _('Used Movie')
        verbose_name_plural = _('Used Movies')


class User (AbstractUser):
    '''
        User of the app, inherits essential fields from AbstractUser

        Important Fields: username, email, password, first_name, last_name
        Important functions: get_full_name
    '''
    avatar_path = models.CharField(
        verbose_name=_('Profile Avatar'),
        max_length=255,
        blank=True, default='',
    )

    movies_watched = models.ManyToManyField(
        to=UsedMovie,
        help_text=_('Movies that the user have watched'),
        related_name='users_watchers',
        blank=True
    )

    movies_favorited = models.ManyToManyField(
        to=UsedMovie,
        help_text=_('Movies that the user have as favorites'),
        related_name='users_fav',
        blank=True
    )

    watch_time = models.IntegerField(
        verbose_name=_('Total Movies Watchtime'),
        help_text=_('Total sum of time watching movies'),
        default=0,
    )

    series_watched = ArrayField(
        models.JSONField(name=_('TV Shows')),
        verbose_name=_('Shows Watched'),
        help_text=_('Shows that the user have watched'),
        blank= True, default=list
    )

    # REQUIRED_FIELDS = ['email']
    # JSON objects format: { original title: "Loki", release_year: 2015, tmdb_ID: 9999 }
    # to be added: favorite movies, favorite series, avatar picture


class FriendList (models.Model):
    '''
        User friend list
        -TO BE DEVELOPED
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friend_list'
    )


#