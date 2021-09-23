from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

import requests, json
from distutils.util import strtobool

from core_app._env import API_KEY_v3
from core_app.forms import RegisterForm
from core_app.models import UsedMovie


base_url = 'https://api.themoviedb.org/3/'
api_key = API_KEY_v3

# Create your views here.
def homepage(request):
    '''
        Home Page VIEW
    '''
    context1 = {}

    return render(request, 'home.html', context1)


def signup(request):
    '''
        View to register a new user
    '''

    user_form = RegisterForm(
        request.POST or None,
        instance=None
    )

    if request.method == "POST":
        print("HELLO POST")
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            temp_path = user_form.cleaned_data.get('custom_avatar_path')
            temp_path = temp_path.split('static')[-1]
            relative_avatar_path = '/static'+temp_path
            new_user.avatar_path = relative_avatar_path

            new_user.save()

            return redirect('core_app:home_page')

    context = {
        'userform': user_form,
    }
    print("Hello VIEW")

    return render(request, 'registration/signup.html', context)


def movies(request):

    popular = requests.get(f'{base_url}discover/movie?api_key={api_key}&\
        sort_by=popularity.desc&page=1').json()['results']
    trending = requests.get(f'{base_url}trending/movie/week?api_key={api_key}&\
        page=1').json()['results']
    streaming_popular = requests.get(f'{base_url}discover/movie?api_key={api_key}&\
        sort_by=popularity.desc&with_watch_monetization_types=flatrate&watch_region=US&page=1').json()['results']
    theatre = requests.get(f'{base_url}movie/now_playing?api_key={api_key}&region=US&page=1').json()['results']
    top_rated = requests.get(f'{base_url}movie/top_rated?api_key={api_key}&page=1').json()['results']

    context = {
        'popular': popular,
        'trending': trending,
        'streaming_popular': streaming_popular,
        'theatre': theatre,
        'toprated': top_rated,
    }

    return render(request, 'movies.html', context)


def get_movie_info(request, tmdb_id):
    '''
        Returns Individual Movie Info given its ID on TMDB
    '''
    
    film = requests.get(f'{base_url}movie/{tmdb_id}?api_key={api_key}&language={request.LANGUAGE_CODE}').json()

    watch_check = False
    fav_check = False
    # To check the watched and favorited boxes if necessary
    if request.user.is_authenticated:
        watch_check = request.user.movies_watched.filter(tmdb_id=tmdb_id).exists()
        fav_check = request.user.movies_favorited.filter(tmdb_id=tmdb_id).exists()

    context = {
        'film': film,
        'series': False,
        'watched': watch_check,
        'favorited': fav_check}

    return render(request, 'individual.html', context)


@login_required
def my_profile(request):
    '''
        Shows current user profile.    
    '''
    user = request.user
    
    context={
        'user': user,
    }
    return render(request, 'profile_self.html', context)


def user_profile(request, user_id):
    '''
        Other users profiles
    '''

    context = {

    }
    return render(request, 'profile_user.html', context)


@login_required
def watch_movie(request):
    '''
        Add the movie to watched list in user object
    '''
    user = request.user
    if request.is_ajax() and request.method == "POST":
        film_data = json.loads( request.POST['data'] )
        print(film_data)
        # JSON/Dict attributes: original_title, release_year, runtime, id
        checked = bool(strtobool( request.POST['check'] ))

        if checked:
            print(checked)
            if not user.movies_watched.filter(tmdb_id=film_data['id']).exists():
                print("Not WATCHED")
                # If the user doesn't already have this movie
                if UsedMovie.objects.filter(tmdb_id=film_data['id']).exists():
                    print("Movie obj EXISTS")
                    # If the movie object exists
                    this_movie = UsedMovie.objects.get(tmdb_id=film_data['id'])
                    user.movies_watched.add(this_movie)
                else: # Else: create new object
                    print("Movie obj DOESNT EXISTS")
                    new_movie = UsedMovie(
                        original_title = film_data['original_title'],
                        release_year = int(film_data['release_year']),
                        duration = int(film_data['runtime']),
                        tmdb_id = film_data['id'],
                    )
                    new_movie.save()
                    user.movies_watched.add(new_movie)
        else: # remove from Watched List
            print(checked)
            if user.movies_watched.filter(tmdb_id=film_data['id']).exists():
                this_movie = UsedMovie.objects.get(tmdb_id=film_data['id'])                
                user.movies_watched.remove(this_movie)

        return HttpResponse(status=200)


@login_required
def fav_movie(request):
    '''
        Add the movie to favorites list in user object
    '''
    user = request.user
    if request.is_ajax() and request.method == "POST":
        film_data = json.loads( request.POST['data'] )
        print(film_data)
        checked = bool(strtobool( request.POST['check'] ))

        if checked:
            print(checked)
            if not user.movies_favorited.filter(tmdb_id=film_data['id']).exists():
                print("Not Favorited")
                # If the user doesn't already have this movie
                if UsedMovie.objects.filter(tmdb_id=film_data['id']).exists():
                    print("Movie obj EXISTS")
                    # If the movie object exists
                    this_movie = UsedMovie.objects.get(tmdb_id=film_data['id'])
                    user.movies_favorited.add(this_movie)
                else: # Else: create new object
                    print("Movie obj DOESNT EXISTS")
                    new_movie = UsedMovie(
                        original_title = film_data['original_title'],
                        release_year = int(film_data['release_year']),
                        duration = int(film_data['runtime']),
                        tmdb_id = film_data['id'],
                    )
                    new_movie.save()
                    user.movies_favorited.add(new_movie)
        else: # remove from Favorited List
            print(checked)
            if user.movies_favorited.filter(tmdb_id=film_data['id']).exists():
                this_movie = UsedMovie.objects.get(tmdb_id=film_data['id'])                
                user.movies_favorited.remove(this_movie)

        return HttpResponse(status=200)
