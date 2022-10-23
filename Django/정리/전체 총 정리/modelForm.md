## 영화 리뷰작성 기능 만들기

### 모델 필드 만들기

우선 아까 유저를 생성하는 것과 다른점은 models.py에서 AbstractUser를 그냥 받아오면 끝이었지만 리뷰작성 기능은 `models.Model`을 받아온 다음 넣고 싶은 속성을 모두 적어 주어야 한다. 그리고 forms.py에서 `UserCreationForm or UserChangeForm` 대신 `forms.ModelForm` 을 받아서 넣고 나머지는 똑같이 Meta를 만들어서 model, fields 등을 넣어주면 된다. 

```python
# reviews/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    grade = models.FloatField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# reviews/forms.py
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "movie_name", "grade"]
        labels = {
            "title": "리뷰 제목",
            "content": "리뷰 내용",
            "movie_name": "영화 제목",
            "grade": "평점(0~5)",
        }
```

#### 팀원덕분에 새로 배운 기능

```python
grade = models.FloatField(
    default=1, validators=[MaxValueValidator(5), MinValueValidator(0)]
)
------------------------
model = Movie
fields = 'all'
exclude = ['created_at', 'updated_at', 'view_count'] # 이걸 사용하면 (전체 - 빼고 싶은것) 을 할 수 있다. 
labels = { # 보이는 이름을 바꿀 수 있다. 
    'title' : '리뷰 제목', 
    'content' : '리뷰 내용',
    'movie_name' : '영화 제목',
    'grade' : '평점(0~10)',
}
```

MaxValueValidator, MinValueValidator을 통하여 백엔드에서 최대값, 최솟값을 지정할 수 있는 기능을 알게되었다. 

### 리뷰 목록 보여주기

#### urls

```python
path("", views.index, name="index"),
```

#### view

```python
def index(request):
    reviews = Review.objects.order_by("-created_at")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)
```

order_by를 사용하여 최신글 순서대로 보여주도록 설정하였습니다. 

#### html

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}
<h1 class="text-center fw-bold">리뷰 목록</h1>
<div class="d-flex justify-content-end">
  <button
    type="submit"
    class="btn btn-outline-dark my-3"
    onclick="location.href='{% url 'reviews:create' %}' "
  >
    작성하기
  </button>
</div>
<table class="table">
  <thead>
    <tr>
      <th scope="col">리뷰 제목</th>
      <th scope="col">영화 이름</th>
      <th scope="col">평점</th>
    </tr>
  </thead>
  <tbody>
    {% for review in reviews %}
    <tr>
      <th scope="row">
        <a
          href="{% url 'reviews:detail' review.pk %}"
          style="text-decoration: none"
          >{{ review.title}}</a
        >
      </th>
      <td>{{ review.movie_name}}</td>
      <td>{{ review.grade }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock content %}
```

### 리뷰 생성하기

#### url

```python
path("create/", views.create, name="create"),
```

#### view

```python
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()

    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context)
```

#### html

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}

<h1>Create</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form review_form %}
  <button type="submit" class="btn btn-outline-dark">생성</button>
</form>
{% endblock content %}
```

### 리뷰 상세 보기

#### url

```python
path("detail/<int:pk>", views.detail, name="detail"),
```

#### view

```python
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)
```

#### html

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}
<h2 class="text-center fw-bold">{{review.title}}</h2>
<hr />
<h3 class="d-flex justify-content-between">
  {{review.movie_name}}<span><small>⭐{{review.grade}}</small></span>
</h3>

<hr />
<p>{{review.content}}</p>

<div class="d-flex">
  <button
    type="submit"
    class="btn btn-outline-dark"
    onclick="location.href='{% url 'reviews:update' review.pk %}' "
  >
    수정
  </button>
  <form
    class="mx-2"
    action="{% url 'reviews:delete' review.pk %}"
    method="POST"
  >
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-danger">삭제</button>
  </form>
</div>
{% endblock content %}
```

[![Animation_2022-10-15-00-31-15](https://github.com/hvvany/movie_login_pair/raw/master/README.assets/Animation_2022-10-15-00-31-15.gif)](https://github.com/hvvany/movie_login_pair/blob/master/README.assets/Animation_2022-10-15-00-31-15.gif)



출처: 김준환님 README.md

이 부분은 팀원분들이 예쁘게 꾸며 주었습니다. 

### 리뷰 수정 및 삭제

#### url

```python
path("detail/<int:pk>/update/", views.update, name="update"),
path('detail/<int:pk>/delete/', views.delete, name='delete'),
```

#### view

```python
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("reviews:index")
    else:
        return redirect("reviews:detail", review.pk)
```

#### html

```html
reviews.update
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}

<h1>Update</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form review_form %}
  <button type="submit" class="btn btn-outline-dark">수정</button>
</form>
{% endblock content %}
```



