from django.shortcuts import render
import requests, json
from core_app._env import API_KEY_v3


base_url = 'https://api.themoviedb.org/3/'
api_key = API_KEY_v3

# Create your views here.
def homepage(request):
    '''
        Home Page VIEW
    '''
    context1 = {}

    return render(request, 'home.html', context1)

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
