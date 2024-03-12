import requests
from bs4 import BeautifulSoup
import pymongo

#mongodb 서버 연결
def conn_db():
    MONGO_SERVER = pymongo.MongoClient("mongodb://localhost:27017/")

    db = MONGO_SERVER["movie_app"]
    collection = db["movies"]
    
    return collection


# cgv 데이터 크롤링
def crawling():
    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'

    response = requests.get(url)
    result = BeautifulSoup(response.text, 'html.parser')

        
    data_img = result.findAll('div', 'box-image')
    data_contents = result.findAll('div', 'box-contents')

    # span 태그의 thumb-image 클래스를 가진 요소만 추출
    data_img = result.findAll('span', 'thumb-image')
    data_title = result.findAll('strong', 'title')
    data_percent = result.findAll('strong', 'percent')
    data_release = result.findAll('span', 'txt-info')


    img_list = []
    title_list = []
    percent_list = []
    release_list = []
    movies = {}
    num = 0

    for item in data_img:
        img_tag = item.find('img')  # span 태그 내의 img 태그 추출
        if img_tag:
            img_url = img_tag['src']  # img 태그의 src 속성 추출
            img_list.append(img_url)  # 이미지 URL을 img 리스트에 추가
            
    for item in data_title:
        title = item.get_text(strip = True)
        if title:
            title_list.append(title)  # 이미지 URL을 img 리스트에 추가
            
    for item in data_percent:
        percent_tag = item.find('span')
        if percent_tag:
            percent = percent_tag.get_text(strip = True)
            percent_list.append(percent)  # 이미지 URL을 img 리스트에 추가
            
    for item in data_release:
        release_tag = item.find('strong')
        if release_tag:
            release = release_tag.get_text(strip = True)
            release_list.append(release[:10])  # 이미지 URL을 img 리스트에 추가
            
    num = len(img_list)

    for i in range(num):
        movie = {
            'title': title_list[i],
            'percent': percent_list[i],
            'release': release_list[i],
            'img' : img_list[i]
        }
        conn_db().insert_one(movie)
