from flask import Flask, Blueprint
from backend.crawling.movie_crawling import conn_db
import pymongo

movie_bp = Blueprint('movie', __name__, url_prefix='/')

movie_bp.route('', methods = ['GET'])
def show_movies():
    movies = []
    
    db_result = conn_db().find()
    
    for item in db_result:
        movie = {
            'title': item['title'],
            'percent': item['percent'],
            'release': item['release'],
            'img' : item['img']
        }
        movies.append(movie)
    print(movies)
    return {
        'movies': movies
    }