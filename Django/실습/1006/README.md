## VSCode에서 Django 템플릿 오토 포매팅하기

아래 3개 설치 및 확인

Unibeautify

Django

Python 

vscode 설정 -> settings.json(오른쪽 위에 위치)

아래 코드 추가

"files.associations": {} 가 있음 그 아래에 붙여넣으면 끝

```python
"files.associations": {
  "**/*.html": "html",
  "**/templates/**/*.html": "django-html",
  "**/templates/**/*": "django-txt",
  "**/requirements{/**,*}.{txt,in}": "pip-requirements"
},
"emmet.includeLanguages": {
  "django-html": "html"
},
"unibeautify.enabled": true,
"[django-html]": {
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "Glavin001.unibeautify-vscode"
}
```

만약 언어 상태를 변경하고 싶으면 오른쪽 아래에 언어를 바꾸는 버튼이 있다. 그걸 클릭하면 된다. 

## 만약 static 사용하려면

if css or js or 이미지 파일 사용 할려면 static를 설정해 준다. 

```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

밖에 static 폴더를 만든후 

{% load static %}(맨 위에)

{% static 'css/style.css' %}(내가 원하는 위치에 위치를 적어준다. )

## 코딩 되새기기

### venv 설치 및 사용

python -m venv venv

. venv/script/active

### 장고 설치및 프로젝트, 앱 생성

pip list

pip install django==3.2.13

pip install black 

django-admin startproject a_pjt_movie (점을 안쓰면 venv랑 분리해서 압축해 보낼때 편하다. )

python manage.py startapp movies

### base.html 만들기

pjt settings에서 앱등록, BASE_DIR 설정->가장 바깔에 templates base.html 파일 만들기

base.html 에서 부트스트랩 가져와 주고 {% block content %}{% endblock %}

### 이후 html파일 만들때

모든 파일에 

{% extends 'base.html' %}

{% block content %}

......

{% endblock %}

을 사용해 주고



ModelForm을 사용해 주면 

{% load django_bootstrap5 %}

{% bootstrap_css %}

{% bootstrap_javascript %}

...

\<form action="" method="post">

 {% csrf_token %}

 {% bootstrap_form article_form %}

\</form>

추가 설정을 해 준다. 

### Model & ModelForm

model class를 만들어 주고

modelForm 에서도 그에 맞게 만들어 준다. 

### ModelForm을 이용한 view 함수 만들기

이 방법의 핵심은 if 와 else를 이용하여 post로 온거랑 get으로 온거랑 우회하여 들어온 것을 구분을 짓고, get 혹은 우회하여 들어오면 해당 페이지를 렌더링 시켜주고, post로 들어오고 우회한것이 아니면 통과시켜 저장을 하는 것이다. 

그리고 업데이트나 삭제는 해당 글을 구분 할 수 있는 것이 필요하므로 pk값을 활용하고 instance를 활용해 준다. 



