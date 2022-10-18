# A one - to - many - relationship

관계형 데이터 베이스 = 표

## 모델 관계

1:1

프로필

1:N

| Comment      | Article    |
| ------------ | ---------- |
| content      | title      |
| created_at   | content    |
| updated_at   | created_at |
| Article의 ID | updated_at |

M:N

아마 회원과 게시글, 댓글과의 관계



## ForeignKey(to, on_delete, **options)

- A one-to-many relationship을 담당하는 Django의 모델 필드 클래스 
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당 
- 2개의 필수 위치 인자가 필요 
  - 참조하는 model class 
  - on_delete 옵션
    - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의 
    - 데이터 무결성을 위해서 매우 중요한 설정 
    - on_delete 옵션 값 
      - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제 
      - PROTECT, SET_NULL, SET_DEFAULT … 등 여러 옵션 값들이 존재 
      - 수업에서는 CASCADE 값만 사용할 예정
- [참고](https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)

## Comments 모델 정의

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작 성됨 
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자) 으로 작성하는 것을 권장 (이유는 이어지는 모델 참조에서 확인 예정)

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ...
    
    def __str__(self):
    	return self.content
```

or

```python
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`

# 댓글 생성 

```
# Comment 클래스의 인스턴스 comment 생성
comment = Comment()
# 인스턴스 변수 저장
comment.content = 'first comment'
# DB에 댓글 저장
comment.save()
# 에러 발생
django.db.utils.IntegrityError: NOT NULL constraint failed: articles_comment.article_id
# articles_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문

# 게시글 생성 및 확인
article = Article.objects.create(title='title', content='content')
article
=> <Article: title>
# 외래 키 데이터 입력
# 다음과 같이 article 객체 자체를 넣을 수 있음
comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에
# 넣어 줄 수도 있지만 권장하지 않음
# DB에 댓글 저장 및 확인
comment.save()
comment
=> <Comment: first comment>

comment.pk
=> 1
comment.content
=> 'first comment'
# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
comment.article
=> <Article: title>
# article_pk는 존재하지 않는 필드이기 때문에 사용 불가
comment.article_id
=> 1

# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1
# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'

comment = Comment(content='second comment', article=article)
comment.save()
comment.pk
=> 2
comment
=> <Comment: second comment>
comment.article_id
=> 1
```

# xxx_set 사용하기

- Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저 
- article.comment 형식으로는 댓글 객체를 참조 할 수 없음 
  - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음 
- 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음 
- 반면 참조 상황(Comment → Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가 능

`$ pip install django-extensions`

세팅

`"django_extensions",`

`$ python manage.py shell_plus`

`article = Article.objects.get(pk=1)`

`dir(article)`로 확인 가능

admin에도 등록하기!!!







comment = Comment.objects.create(article='13', content='111')

comment.article <Article: Article object (13)>

comment.article_id 13

comment.article.object.all()???

article.comment_set.all() 모든 댓글

Comment.objects.filter(article_id=13)



A 모델 B 모델 FK 정의. B모델 A모델 어떻게 쓸까요?

:b.a_set

# 댓글 생성

```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.order_by("-pk")
    context = {
        'comments': comments,
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

comments = article.comment_set.all()

모델폼의 save메서드는 리턴 값이 그 모델의 인스턴스이다. 

```python
# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

```html
<h4>댓글 목록</h4>
<ul>
    {% for comment in comments %}
    	<li>{{ comment.content }}</li>
    {% endfor %}
</ul>
<hr>
```



# 댓글 삭제

```python
# articles/urls.py
urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```

# 댓글 관련 추가 기능

## 댓글 갯수 출력하기

```html
DTL filter - length 사용
{{ comments|length }}
{{ article.comment_set.all|length }}

Queryset API - count() 사용
{{ comments.count }}
{{ article.comment_set.count }}
```

```html
<!-- articles/detail.html -->
<h4>댓글 목록</h4>
{% if comments %}
	<p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

## 댓글이 없는 경우

```html
{% for comment in comments %}
    <li>
    {{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
    </form>
    </li>
{% empty %}
	<p>댓글이 없어요..</p>
{% endfor %}
```





















