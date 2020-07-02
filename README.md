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
