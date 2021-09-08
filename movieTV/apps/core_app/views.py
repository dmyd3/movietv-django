from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests, json
from core_app._env import API_KEY_v3
from core_app.forms import RegisterForm


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
            print("HELLO VALID USER")
            print(new_user)
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
    

    context = {
        'film': film,
        'series': False}

    return render(request, 'individual.html', context)