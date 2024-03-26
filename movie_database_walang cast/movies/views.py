from django.shortcuts import render
import requests


import random

def index(request):
    api_key = 'a209dc096e1611ec93f71bf8b9b05127'
    random_page = random.randint(1, 10)
    recommended_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={random_page}'
    recommended_response = requests.get(recommended_url)
    
    if recommended_response.status_code == 200:
        recommended_data = recommended_response.json()
        recommended_movies = recommended_data.get('results', [])
    else:
        recommended_movies = []

    return render(request, 'index.html', {'recommended_movies': recommended_movies})



def search_movies(request):
    query = request.POST.get('query')
    if query:
        api_key = 'a209dc096e1611ec93f71bf8b9b05127'
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            search_results = data.get('results', [])

            for movie in search_results:
                movie_id = movie.get('id')
                cast_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
                cast_response = requests.get(cast_url)
                if cast_response.status_code == 200:
                    cast_data = cast_response.json()
                    cast_list = cast_data.get('cast', [])
                    movie['cast'] = cast_list[:3]
                else:
                    movie['cast'] = None

            return render(request, 'search_results.html', {'query': query, 'search_results': search_results})
        else:
            error_message = 'Failed to fetch search results from TMDB API'
            return render(request, 'search_results.html', {'query': query, 'error_message': error_message})
    else:
        return render(request, 'index.html')

def search_results(request):
    genre = request.GET.get('genre')

    api_key = 'a209dc096e1611ec93f71bf8b9b05127'
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&region={country}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        search_results = data.get('results', [])

        for movie in search_results:
            movie_id = movie.get('id')
            cast_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
            cast_response = requests.get(cast_url)
            if cast_response.status_code == 200:
                cast_data = cast_response.json()
                cast_list = cast_data.get('cast', [])
                movie['cast'] = cast_list[:3]
            else:
                movie['cast'] = None

    else:
        search_results = []

    return render(request, 'search_results.html', {'genre': genre, 'search_results': search_results})
