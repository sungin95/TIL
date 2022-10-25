

요청: http, get, post, url(path)

응답: html, status code

서버와 DB는 다르다?

서버: views.py

모델: ORM



단일객체 (개별)

쿼리셋 (박스)



1:N??? 이 관계 아직 잘 모르겠다.



# User가 User받기



## model

```python
# accounts/models.py

class User(AbstractUser):
	followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

특징적인게 self를 받아 준다. 

```
$ python manage.py makemigrations
$ python manage.py migrate
```

## 구현

url

```python
# accounts/urls.py
urlpatterns = [
	...,
	path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

view

```python
# accounts/views.py
def follow(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

html

```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
        <div>
        	팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
        </div>
        {% if request.user != person %}
            <div>
                <form action="{% url 'accounts:follow' person.pk %}" method="POST">
                    {% csrf_token %}
                    {% if request.user in person.followers.all %}
                        <input type="submit" value="Unfollow">
                    {% else %}
                        <input type="submit" value="Follow">
                    {% endif %}
                </form>
            </div>
        {% endif %}
    </div>	
```

추가 구현

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
		....
        ....
        ....
    return redirect('accounts:login')
```





# View decorators & functions

html을 응답한다 반환한다???

views.py

- render 2xx html

- redirect 3xx html

- @login_required 302

- 주소창 잘못 적으면 400에로

- 서버에 잘못되면 () 500

- 해당 쿼리셋이 없을 때 1000

  - 사용자가 임의로 주소창을 입력했을때 겟을 땡겨왔는데 그런 아티클은 없어요..?

    - 이 상황이면 억울하니까(유저가 잘못했는데)

    - article = get_object_or_404(Article, pk=pk)

    - view

      ```python
      from django.shortcuts import render, redirect, get_object_or_404
      
      def detail(request, pk):
          user = get_object_or_404(get_user_model(), pk=pk)
          ...
      ```

      



redirect 는 get 이다. URL 



내일 자바스크릿트 로또 보고 오자!!!



## 메서드 목록 

- require_http_methods() 

  - ```python
    # views.py
    
    from django.views.decorators.http import require_http_methods
    
    @require_http_methods(['GET', 'POST'])
    def create(request):
    	pass
    
    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
    	pass
    ```

- require_POST() 

  - ```python
    # views.py
    
    from django.views.decorators.http import require_http_methods, require_POST
    
    @require_POST
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    ```

  - ```
    Method Not Allowed (GET): /articles/3/delete/
    [04/Jan/2022 04:52:10] "GET /articles/3/delete/ HTTP/1.1" 405 0
    ```

- require_safe()

  - ```python
    # views.py
    
    from django.views.decorators.http import require_http_methods, require_POST, require_safe
    
    @require_safe
    def index(request):
    	...
        
    @require_safe
    def detail(request, pk):
    	...
    ```



## (참고) @login_require와 require_POST

- 핵심: next의 값은 get으로 값을 보낸다. 
- 상황 
  - 비로그인 상태로 detail 페이지에서 게시글 삭제 시도 
  - delete view 함수의 @login_required로 인해 로그인 페이지로 리다이렉트 
    - http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/ 
  - redirect로 이동한 로그인 페이지에서 로그인 진행 
    - redirect는 반드시 GET요청으로만 가능 
  - delete view 함수의 @require_POST로 인해 405 상태 코드를 받게 됨 
    - 405(Method Not Allowed) status code 확인 
- @login_required는 GET 요청을 처리하는 View 함수 에서만 사용해야 함
- 로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트

### 그러면 @require_POST를 사용한 경우 어떻게 로그인을 체크 할까?

- POST method만 허용하는 delete 같은 함수는 내부에서는 is_authenticated 속성 값을 사용해서 처리

- ```python
  # articles/views.py
  
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = Article.objects.get(pk=pk)
          article.delete()
      return redirect('articles:index')
  ```

  











