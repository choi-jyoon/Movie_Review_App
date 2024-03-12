from flask import Flask, Blueprint
from crawling.movie_crawling import conn_db
import pymongo

app = Flask(__name__)

# movie Blueprint 생성
movie_bp = Blueprint('movie', __name__, url_prefix='/movies')

@movie_bp.route('', methods=['GET'])
def show_movies():
    movies = []
    
    # 여기에서 영화 정보를 가져오는 로직을 구현하세요.
    # 예를 들어, movie_crawling 모듈을 사용하여 데이터를 가져올 수 있습니다.
    
    # 예시 코드
    db_result = conn_db().find()
    id = 0
    
    for item in db_result:
        id+=1
        movie = {
            'id': id,
            'title': item['title'],
            'percent': item['percent'],
            'release': item['release'],
            'img': item['img']
        }
        movies.append(movie)
    
    print(movies)
    return {
        'movies': movies
    }

# Flask 애플리케이션에 Blueprint 등록
app.register_blueprint(movie_bp)

# 루트 경로에 대한 라우트 추가
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
