import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTQ2YjM0N2ZiNzNjNjlmYzQ0ZWYxNT" \
            "c0YzZjODM4YiIsInN1YiI6IjVlZjA5ZWIzNTY4NDYzMDAzNDAzNTgxMSIsInNjb" \
            "3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wKUOWsYecNdbSyFBU_Dzd" \
            "zJEBSLnqIMPtek_eqrUzws"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_name="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    random.shuffle(data["results"])
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
