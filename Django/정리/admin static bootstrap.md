# admin

## 사용을 위해 임시 계정을 만든다. 

python manage.py createsuperuser



[관련 장고문서](https://docs.djangoproject.com/ko/3.2/intro/tutorial07/)

```python
from django.contrib import admin
from .models import Article 


class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "content"]


admin.site.register(Article, ArticleAdmin) # 여기에 나의 모델을 등록해야 한다. 
```

# static

스태틱을 사용하면 절대 경로를 통하여 파일을 갖고 올 수 있어 사용하는 파일의 위치가 바뀌어도 값을 변경 할 필요가 없다. 

## 사용 방법

프로젝트의 settings 에서 

```python
STATIC_URL = '/static/' (처음 기본값으로 설정 되어 있다.)
여기에 
import os와
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "static"),
]
를 설정해 준다. 
```

static 폴더 안에 필요한걸 넣고 사용하면 된다. 

static폴더의 위치는 밖에 두어도 앱폴더 안에 넣어도 되지만 이 이상 깊이 넣으면 작동이 안되고 

그리고 html 파일에는 

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %} " />
```



[장고 부트스트랩](https://pypi.org/project/django-bootstrap5/)

`$ pip install django-bootstrap5`

settings.py 에서 엡등록

```python
INSTALLED_APPS = (
    # ...
    "django_bootstrap5",
    # ...
)
```



```html
{% load django_bootstrap5 %} 
{% bootstrap_css %} 
{% bootstrap_javascript %}
<h1>글쓰기</h1>
<form action="{% url 'articles:create' %}" method="post">
  {% csrf_token %} 
    {% bootstrap_form article_form %} 
    {# article_form.as_p #}
  <input type="submit" value="글쓰기" />
  {% bootstrap_button button_type="submit" content="OK" %}
</form>
```



장고 모델폼 커스텀마이징

