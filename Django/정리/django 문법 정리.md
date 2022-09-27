# 문법

터미널 문법

pwd

cd ~

mkdir



가상환경 생성

```$ python -m venv venv```(venv생성)

```$ source venv/Scripts/activate```(실행)

```$ pip list```   (체크)

```$ deactive```   (끄기)

`$pip install django==3.2.13 ` (장고 설치)

```$ django-admin startproject firstpjt .``` 장고 파일 설치

`$python manage.py runserver` 장고 파일 실행

`$python manage.py startapp` 장고 파일 실행

`$ rm -r test-venv` (venv삭제)



그후 settings.py에 앱 이름 등록

urls.py에서 path를 등록해 준다. 



# 장고 html문법

## base

{% block content %} 

{% endblock %}



{% extends 'base.html' %} 

{% block content %}

{% endblock %}



{{ 변수명 }}

## for

{% for w in words %}

{% endfor %}



# views 문법

```python
print(request)

print(dir(request))

print(request.GET.get('ball'))

name = request.GET.get('ball')
```



# base문서 만들기 

최상단에 templates를 만들고

settings.py 에서 

"DIRS": [BASE_DIR/'templates'],



# url나누기

```python
from django.urls import path, include

path('articles/'include('articles.urls')),
```







# form에서 받고 저장

```html
<form action='/articles/create/'>
    <input type='text' name='content'>
    <input type='submit'>
</form>
```





이제 셀에서 명령하는 것처럼 views.py의 함수에 

```python
from .models import Article
Article.objects.create(content=content)
```

# 명령어 정리 

```python
guestbook = Ariticle.objects.all()
# SELECT * FROM articles;
content = request.GET.get('content')
# guestbook.append(content)
# DB에 저장
Article.objects.create(content=content)

출력: {{ content.content }}
```















