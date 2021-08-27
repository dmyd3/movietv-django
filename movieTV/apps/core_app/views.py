from django.shortcuts import render

# Create your views here.
def homepage(request):
    '''
        Home Page VIEW
    '''
    context1 = {}

    return render(request, 'home.html', context1)

def movies(request):

    context1 = {}
    return render(request, 'movies.html', context1)