import requests
import random


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTQ2YjM0N2ZiNzNjNjlmYzQ0ZW" \
                "YxNTc0YzZjODM4YiIsInN1YiI6IjVlZjA5ZWIzNTY4NDYzMDAzNDAzNTgxM" \
                "SIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wKUOWsYec" \
                "NdbSyFBU_DzdzJEBSLnqIMPtek_eqrUzws"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    random.shuffle(data["results"])
    return data["results"][:how_many]