# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

-   [ ] List Rooms
-   [ ] Filter Rooms
-   [ ] Search By Coords
-   [ ] Login
-   [ ] Create Account
-   [ ] See Room
-   [ ] Add Room to Favourites
-   [ ] See Favs
-   [ ] See Profile
-   [ ] Edit Profile

# 0. Introduction

## 0.2 How to get the base files

-   노마드에서 블루프린트 클론
-   원하는 디렉토리에서 git clone https://github.com/nomadcoders/airbnb-api --branch blueprint --single-branch new-airbnb-api
-   깃허브에서 새로운 레포를 만들고 클론한걸 옮겨야함
-   디렉토리에서 rm -rf .git
-   git init
-   git remote add origin 새로운 레포 주소
-   git add .
-   git commit -m "init"
-   git push origin master

## 0.3 Explaining the Base File

-   pipenv install
-   python manage.py makemigrations
-   python manage.py migrate
-   python manage.py createsuperuser
-   pipenv update django-seed
-   python manage.py mega_seed

## 0.4 Goals and Tools

-   REST와 GraphQL api를 섞어서 사용할것임, 근데 원래 섞어서 쓰진 않음
-   REST api 가 더 좋다, django rest framework가 있어서
-   Graph QL은 node.js랑 잘어울림

## 0.6 Intro to REST API's

-   REST api는 서버와 서로 의사 소통을 하는 URL을 사용하는 api
-   yts.lt 사이트 api 참고, url마다 제공받는게 다 다름

## 0.7 Beautiful REST part one

-   무언가를 요청할때는 GET 요청을함
-   로그인할때 비밀스러운 form을 이용해서 보낼때는 POST
-   REST API DESIGN
-   api에서 동사들을 사용하지 말자 ex) list_movie -> 나쁨
-   명사는 좋고
-   복수형은 더 좋음
-   getAllMoviews,addMovies,deleteMovies -> 이런건 나쁜거다
-   CRUD
-   Create - Post
-   Read - Get
-   Update - Put
-   Delete - Delete
-   /movies/ -> Collection
-   /movies/the-godfather -> Elements
-   Formula : Collections + Elemetns + HTTP Verbs

## 0.8 Beautiful REST part two

-   "?"를 사용한다
-   /movies?status=now_showing
-   collection을 사용하면서 ?를 이용해 쿼리인자를 사용하면 됨
-   Version & Pages
-   /v1/movies
-   HTTP
-   200 ok
-   201 created
-   400 bad request
-   403 forbidden
-   404 not found
-   500 interner server error
-   501 not implemented

# 1. INTRODUCTION TO DRF

## 1.1 @api_view

-   pipenv install djangorestframework
-   config/settings 에 third party app 추가
-   THIRD_PARTY_APPS = ["rest_framework",]

## 1.2 Serializers

-   Serializer는 기본적으로 데이터가 보여야하는 방식을 설명해줘야 하는 form이다.
-   대신 json 방식이어야함
-   모델들의 객체를 검증해서 json으로 변경해줌
-   즉 파이썬 객체에서 JSON 객체로 바꿔주는것을 의미한다.

## 1.3 Class Based View

-   Pagination을 사용하기 위해 setting.py 에 추가
-   REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    }

## 1.4 ListAPIView

-   [x] ListRooms
-   [v] SeeRoom

## 1.6 ModelViewset

-   viewsets를 사용하면 뭐 아무것도 없이 전부다 가능해짐
-   패지네이션이나 post,get,delete,put 전부
-   근데 아무나 막 수정할수 있으면 안되니 약간의 논리가 필요

# 2. BUILDING THE REST API

## 2.1

-   [x] ListRooms
-   [x] SeeRoom

## 2.4

-   post인지 put의 차이는 put에는 instance값이 있음
-   instanace가 first arguement면 serializer가 create이 아닌 put하고 있다고 인식
-   serializer의 모든 데이터를 수정할 필요없이 몇개만 수정하고싶으면 partial=True, 안그러면 시리얼라이저의 모든 모델값들에 대해 데이터가 주어져야함

## 2.11 JWT

-   JWT 는 유저에게 긴 스트링을 주고 유저가 해독함
-   스트링을 가져옴 유저아이디든 이메일이든
-   이걸 인코딩해서 이상한 값으로 바꿈 (토큰)
-   유저는 인코딩된걸 다시 우리한테주고
-   우리는 그걸 다시 디코딩
-   파이썬 JWT 은 설치해야함 pyJWT
-   pipenv install pyjwt
-   절대 jwt에 민감한 개인정보를 담아선 안됨 누구나 토큰 해독을 할 수 있음
-   그럼 뭐하러 쓰냐?
-   누가 우리 토큰을 건들엇냐 안건드렷냐 이걸 확인하기 위해 씀
