# 이미지 등록 & widget & 메시지

## pip install 

1. django==3.2.13
2. black
3. django-bootstrap5
4. Pillow
5. pip install django-imagekit
6. pip install django-widget-tweaks
7. pip freeze > requirements.txt



## settings

### 기본

```python
"DIRS": [BASE_DIR / "templates"],

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```







### 앱 등록

```python
INSTALLED_APPS = [
  "articles",
  "imagekit",
  "django_bootstrap5",
]
```



### 설정

```python
MEDIA_ROOT = BASE_DIR / 'media' # 
MEDIA_URL = '/media/' 

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage" # 메시지

INSTALLED_APPS += [ # widget
    "widget_tweaks",
]
```





## URL

```python
# 프로젝트 폴더의 urls.py
...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ....
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



## 모델 설정

### models.py

```python
# articles/models.py

class Article(models.Model):
    title = ....
    ...
    image = models.ImageField(blank=True, upload_to='images/')
    

# 이미지 resize
# models.py
...
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail

class Article(models.Model):
    ...
    image = models.ImageField(blank=True, upload_to="images/")
    thumbnail = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )
```

### forms.py 

(다른점은 없지만 편의를 위하여)

```python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image", "thumbnail"]
        labels = {
            "title": "제목",
            "content": "내용",
            "image": "이미지",
            "thumbnail": "썸네일",
        }
```





## views.py

```python
from django.contrib import messages

form = ArticleForm(request.POST, request.FILES)
messages.success(request, "글 작성이 완료되었습니다.")
```





## html

```html
<!-- articles/create.html -->

{% extends 'base.html' %}
{% load widget_tweaks %}
{% load django_bootstrap5 %}
{% block content %}
  <form action="" method="post" class="form" enctype="multipart/form-data"> <!-- 인코딩을 해주어야 한다.   -->
    {% csrf_token %}

    {% bootstrap_form article_form %}

    {% bootstrap_button button_type="submit" content="OK"%}
    {% bootstrap_button button_type="reset" content="Cancel"%}
      
    {% render_field article_form.title type="search"%} <!-- widget -->
  </form>
{% endblock content %}



<!-- articles/index.html -->
{% extends 'base.html' %}
{% block content %}
  {% if messages %} <!-- 메시지 -->
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }}">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
  <a href="{% url 'articles:create' %}">create</a>
  {% for article in articles %}
    <div class="card" style="width: 18rem;">
      <img src="{{ article.thumbnail.url }}" class="card-img-top" alt="{{article.image}}"> <!-- 이미지 -->
      <div class="card-body">
        <h5 class="card-title">{{article.title}}</h5>
        <p class="card-text">{{article.content}}</p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">자세히</a>
      </div>
    </div>
  {% endfor %}
{% endblock content %}
```

### 확인

검사창에 들어가서`accept="image/*"` or `이미지 파일` 인지

[widget기능](https://pypi.org/project/django-widget-tweaks/)