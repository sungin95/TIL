# 만든 계기

이번주 내용이 너무 복잡해서 한번 정리하고 가야 할거 같아서 만들었습니다. 





# 1014 페어 프로그래밍 정리

우선 1번분이 처음에 .gitignore을 만들고 

사람들 초대를 한다. 

2번분이 받아서 프로젝트랑 앱을 만들고 django==3.2.13, black, bootstrap5을 설치하고 3번분에게 넘긴다. 

3번분부터 시작한다. 

오늘의 실습은 지난주와 이번주 배운 것을 총 정리 하는 느낌이었습니다. 

그리고 특징적으로 깃허브를 이용한 협업이었습니다.  방법은

```
$ git checkout -b "accounts/signup" # 깃허브 생성 및 전환
...
...
... 작업후
$ git add . 
$ git commit -m "name"
$ git push origin accounts/signup
(깃허브에 가서 머지를 한다.)
$ git checkout master
$ git pull origin master
$ git branch -b accounts/signup
만들었던 브런치까지 삭제하면 끝
```



## 기본 세팅

앱이름: accounts

우선 앱을 등록을 해 주고 

base.html폴더 파일까지 제작해 준다. 

base.html은 nav바와 bootstrap을 사용 할 수 있게 준비 해 준다. 

이제 pjt에서 ulrs.py include를 사용하여 

accounts.ulrs로 설정을 해 준다. 

(app_name은 "accounts"로 해 주자)

# 정리하면서 새롭게 안 내용 정리

## forms.Form

그냥 Form은 생성하는 기능이 없어서 체크, 인증에 주로 쓰인다. (비밀번호는 유저 정보에 관한건데 왜 Form에서 관리되는 지는 모르겠다. )

forms.Form: AuthenticationForm, PasswordChangeForm

> AuthenticationForm -forms.Form-BaseForm(공통)

> PasswordChangeForm - SetPasswordForm - forms.Form - BaseForm(공통)

## forms.ModelForm

ModelForm은 DB에 새롭게 추가하거나 업데이트 할때 사용한다. 

forms.ModelForm: UserCreationForm, UserChangeForm

> UserCreationForm - forms.ModelForm-BaseModelForm - BaseForm(공통)
>
> UserChangeForm - forms.ModelForm - BaseModelForm - BaseForm(공통)

### 사용한 메서드 저장된 위치

BaseForm: is_vaild

BaseModelForm: save

> UserCreationForm - forms.ModelForm-BaseModelForm(우리가 쓰는 save는 여기서 가져 온다. ) - BaseForm(is_vaild()는 이곳에 있다. )



## request vs request.GET vs request.POST 출력 비교

|               | request                                                     | request.GET                                 | request.POST                                                 |
| ------------- | ----------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| 프린트 예시   | <WSGIRequest: GET '/accounts/login/?next=/accounts/index/'> | <QueryDict: {'next': ['/accounts/index/']}> | <QueryDict: {'csrfmiddlewaretoken': ['REvvGOxFcdZI32nCFw2wLdWHGqUB47qmfJaHH3ZnD2TEhk109Ec98wUBsp31kPHM'], 'username': ['sun123'], 'password': ['12345678']}> |
| POST로 보낼때 | GET 인지 POST 인지 그리고 주소창                            | 주소창중 ? 이후의 내용                      | POST로 보낼 시 input으로 들어온 값들이 나온다.               |



## 회원가입과 로그인(로그아웃) 과정

### 우선 user 커스텀 폼을 만들자

회원가입은 기존의 modelForm과 비슷하면서도 다릅니다.

비슷한 부분: view.py에서 함수를 만들때 그 구조가 비슷하다는 것입니다.

다른 점: 불러와야 하는 클래스가 다르고 이 클래스를 찾기 위해서 **내부의 로직을 가져와야 한다**는 것입니다.

### 지금 하는 작업은 이 내부 클래스 로직을 가져오는 것입니다.

작업순서는 `models -> forms`

#### models

우선 model을 만들어 줍니다. 

models.py에서 클래스를 만드는데 이때 특징적인 것이 `model.Model`을 넣은 자리에 `AbstractUser`를 대신 넣는다는 것입니다.  

그리고 `AbstractUser` 는 내부 자체 로직에 속성을 이미 갖고 있어 추가로 속성을 지정하지 않고 pass를 사용합니다. 

이 AbstractUser는 `from django.contrib.auth.models import AbstractUser`에서 가져 옵니다. 

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # AbstractUser 내부에 models.Model을 이미 갖고 있다. 
    pass # 내부 자체 로직에 속성이 이미 있다. 
```

##### settings 설정

이때 settings.py 에서도 추가 설정이 필요하다.

`AUTH_USER_MODEL = 'accounts.User'`을 추가해 주자. 



#### forms

폼을 만드는 방법은 기존 modelForm과 내용은 비슷하지만 불러와야 하는 코드가 달라서 완전히 다르게 보입니다. 

##### modelForm

```python
from .models import Review # 1
from django import forms # 2


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "movie_name",
            "grade",
            "content",
        ]
```

##### userModelForm

```python
from django.contrib.auth import get_user_model # 1
from django.contrib.auth.forms import UserCreationForm # 2


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):# 3
        model = get_user_model()
        fields = ("username", "email")
```

서로 다르게 보이지만 자세히 뜯어보면 이 둘은 같다. 

###### get_user_model(# 1) 내부 코드 

Ctrl + 클릭 을 해서 소스 코드를 보면 `settings.AUTH_USER_MODEL`에서 값을 가져 오는 것을 볼 수 있고, 아까 설정으로 `AUTH_USER_MODEL = 'accounts.User'`를 해 주었기 때문에 User클래스를 갖고 오게 된다. 

그러므로 `# 1`은 모양만 다르지 비슷한 구조라고 볼 수 있다. 

이걸 쓰는 이유는 이 코드에서 볼 수 있듯이 에러가 났을때 관련 메시지를 보낼 수 있기 때문인거 같습니다. 

**핵심: 6번째줄**

```python
def get_user_model():
    """
    Return the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False) # 우리가 세팅한 값에서 값을 가져 오고 있다. 
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )
```



###### UserCreationForm(# 2)

> ​	UserCreationForm - forms.ModelForm-BaseModelForm - BaseForm

`class ReviewForm(forms.ModelForm):`에서

`class CustomUserCreationForm(UserCreationForm):`로 바뀌었지만

UserCreationForm의 코드를 보면 똑같이 forms.ModelForm을 받고 있다. 

**핵심: forms.ModelForm을 받고 있고 password1,password2가 코드로 이미 구현되어 있다. **

```python
class UserCreationForm(forms.ModelForm): # forms.ModelForm을 받고 있다.
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
        
	......
```

forms.ModelForm받는것과 차이점은 password1과 password2를 받고 있다. (회원가입시 비밀번호를 필수로 받는 이유)

###### Meta(UserCreationForm.Meta)(# 3)

`UserCreationForm.Meta`의 유무의 차이는 

|                              | fields가 없을 때                     |
| ---------------------------- | ------------------------------------ |
| Meta:                        | fields를 찾을 수 없다는 오류가 뜬다. |
| Meta(UserCreationForm.Meta): | User의 모든 요소가 출력              |



## 회원가입자 목록

index에서 목록을 보여 주도록 하자!

### index 만드는 순서(urls -> views -> html)

urls.py에서 path 설정과 실행할 함수 지정, 이름을 지정해 준다. 

### urls

```python
from django.urls import path
from . import views

path("", views.index, name="index")
```

### views

views.py에서 index함수를 만들어 준다. 

(참고 앞으로 `User`대신`get_user_model()`을 사용한다. )

```python
def index(request):
    users = get_user_model().objects.all() # 저장된 모든 User를 가져온다. 
    context = {
        'users':users,
    }
    return render(request, "accounts/index.html",context)
```

### html

templates/accounts 폴더를 만든다. 

그리고 bootstarp에서 테이블을 가지고 와서 붙이고 

for문을 사용하여 index함수의 users를 하나하나 불러온다. 

```html
{% extends 'base.html' %} 
{% load django_bootstrap5 %} 
{% block content %}
<h1>회원 목록</h1>
<table class="table">
  <thead>
    <tr>
      <th scope="col">user</th>
      <th scope="col">email</th>
      <th scope="col">last_login</th>
    </tr>
  </thead>
  <tbody>
    {% for user in users %}
    <tr>
      <th scope="row"><a href="{% url 'accounts:detail' user.pk %}">{{ user.username}}</a></th>
      <td>{{ user.email}}</td>
      <td>{{ user.last_login}}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

{% endblock content %}
```



## 회원가입 만들기

여기까지 했으면 회원가입에 필요한 폼 CustomUserCreationForm()클래스를 생성을 완료 했고 view함수에 적용시켜주면 된다. 



회원가입과 동시에 로그인까지 가능하게 하고 싶으면 form.save()을 한 값을 변수화 해서 auth_login()함수에 request랑 같이 넣어주면 된다. 

```python
user = form.save() # POST로 들어온 정보를 CustomUserCreationForm에서 받아서 저정하고 그 값을 바로 로그인 하는데 사용한다. 
auth_login(request, user) # 회원가입과 동시에 로그인을 시키기 위해 
```

### urls

```python
path("signup/", views.signup, name="signup"),
```

### views

```python
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 회원가입과 동시에 로그인을 시키기 위해 
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

### html

```html
{% extends 'base.html' %} 
{% load django_bootstrap5 %} 
{% block content %}

<h1>signUp</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form form %}
  <button type="submit" class="btn btn-outline-dark" >제출</button>
</form>
{% endblock content %}
```

## 로그인과 로그아웃

### urls

```python
path("login/", views.login, name="login"),
```

### views

형식은 똑같고 Form과 save와 같은 메서드 대신 auth_login함수를 사용한다. 

```python
def login(request):
    if request.user.is_authenticated: # 로그인이 된 상태에서는 로그인 화면에 들어갈 수 없다. 
        return redirect("accounts:index") 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # request가 없어도 잘 돌아가는거 같음 하지만 대부분이 request를 필수적으로 받아 가지고 편의상 넣겠음
        if form.is_valid():
            auth_login(request, form.get_user()) # login을 가져와야 한다. 
            return redirect(request.GET.get("next") or "accounts:index") # login_required를 사용하기 위해 
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:login")
```

> AuthenticationForm -forms.Form-BaseForm

로그인을 위해서는 `AuthenticationForm`폼과 `auth_login()` 필요한데. 따로 제작해 줄 필요없이 불러서 쓰기만 하면 된다. 

불러오는 방법은 

`from django.contrib.auth.forms import AuthenticationForm`

`from django.contrib.auth import login as auth_login`

`from django.contrib.auth import logout as auth_logout`

AuthenticationForm 폼에 정보를 넣어줄때 `data=request.POST` 로 data변수를 만들어 줘야 한다. 이름을 바꾸어도 안된다. 

`form = AuthenticationForm(data=request.POST)`(request는 빼도 잘 돌아가는거 같다. )

#### login_required

`login_required`를 통하여 로그인 화면에 들어온 경우에 주소창에 next라는 이름으로 로그인이 되면 돌아갈 주소가 뜨게 된다. 이 next가 있으면 next를 먼저 처리하고 없으면 원래 보내려던 화면으로 보내기 위해 `return redirect(request.GET.get("next") or "accounts:index")`를 사용한다. 

#### login, logout

```python
auth_login(request, form.get_user()) # login은 아직 request.user가 정보가 없는 상태이기 때문에 변수화된 유저정보를 get_user()이라는 메서드를 사용하여 따로 넣어줘야 한다. 
auth_logout(request) # request에 user정보가 이미 있기 때문에 따로 안 넣어 줘도 되는거 같다. 
```

### html

```html
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block content %}
  <h1>login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button type="submit" class="btn btn-outline-dark" onclick="location.href='{% url 'accounts:index' %}' ">로그인</button>

  </form>
{% endblock content %}
```



## 비밀번호 바꾸기(change_password)

> PasswordChangeForm - SetPasswordForm - forms.Form - BaseForm(공통)

PasswordChangeForm역시 불러서 쓰기만 하면 된다.

`from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm` 

비밀번호를 바꿀려면 우선 해당 유저 정보를 불러와야 한다. 그래서 

`PasswordChangeForm(request.user)` request.user가 필수 이다. 



또한 비밀번호를 바꾸게 되면 서버에 저장이 되어 있던 세션에서 문제를 일으킨다. 

서버에 저장된 세션은 응답을 요청한 브라우저에게 쿠키와 세션 id를 주는데. 이 세션id가 해당 유저와 일치하면 로그인을 유지시킨다. 하지만 비밀번호를 바꾸어서 유저 정보가 달라지게 되고 세션은 해당 유저가 잘못된 유저라고 판단을 하고 로그아웃을 시켜 버린다. 물론, 그냥 다시 로그인을 하면 되지만 유저의 편의성을 위해 로그인을 시켜 줄려면 세션값을 새롭게 업데이트를 해 주어야 한다. 그걸 도와주는 명령어가 `update_session_auth_hash`이고 

`from django.contrib.auth import update_session_auth_hash`을 통하여 불러온다. 

### url

```python
path('password/', views.change_password, name='change_password'),
```

### views

```python
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)
```

### html

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}

<h1>비밀번호 수정</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form form %}
  <button type="button" class="btn btn-outline-dark" >수정</button>
  <button type="button" class="btn btn-outline-dark" onclick="location.href='{% url 'accounts:index' %}' ">돌아가기</button>
</form>
{% endblock content %}
```



## 유저 상세 정보(detail)

### url

```python
path('<int:pk>/', views.detail, name="detail"),
```

### views

```python
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)
```

### html

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}
<h1>상세 회원 정보</h1>
<table class="table">
  <thead>
    <tr>
      <th scope="col">user</th>
      <th scope="col">email</th>
      <th scope="col">last_login</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">{{ user.username}}</th>
      <td>{{ user.email}}</td>
      <td>{{ user.last_login}}</td>
    </tr>
  </tbody>
</table>
<button type="button" class="btn btn-outline-dark" onclick="location.href='{% url 'accounts:index' %}' ">돌아가기</button>
{% endblock content %}
```



## 회원 탈퇴

프로젝트에서는 까먹고 구현을 안했지만 구현 할려면 

### url

```python
path("delete/", views.delete, name="user_delete"),
```

### view

```python
def delete(request):
    request.user.delete() 
    auth_logout(request)
    return redirect("accounts:login")
```

왜 request.user.delete() 가 왜 가능한지는 아직 모르겠다. Ctrl + click 을 해 봐도 나오는게 없다. 

## 회원 정보 수정

> UserChangeForm - forms.ModelForm - BaseModelForm - BaseForm(공통)

### url

```python
path("update/", views.update, name="update"),
```

전에랑 다른것은 로그인된 유저의 정보만 바꾸는 작업이기 때문에 url에서 \<int:pk>를 사용 할 필요가 없다. 

그리고 함수에서 instance=request.user 이렇게 받는데 이 user값을 통하여 pk값을 알아내는거 같다. 

### view

```python
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context=context)
```

instance로 request.user를 받는다 말고는 기존 modelForm의 업데이트랑 똑같다. 

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block content %}

<h1>update</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form form %}
  <input type="submit" value="제출" />
  <button type="button" class="btn btn-outline-dark" onclick="location.href='{% url 'accounts:index' %}' ">돌아가기</button>
</form>
{% endblock content %}
```



## @login_required

홈페이지에 로그인이 안되면 들어갈 수 없게 해야 할 때가 있다. 그럴때 해당 함수 바로 위에 @login_required를 걸어주면 자동으로 login페이지로 보내준다. 그리고 'next'를 만들어주고 로그인페이지에서 next를 처리하는 코드를 만들면 로그인이 되고 난 다음 아까 페이지로 돌아간다. 



## 네이바 만들기

```html
{% load django_bootstrap5 %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Document</title>
    {% bootstrap_css %}
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'accounts:index' %}">Movie</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            {% if request.user.is_authenticated %}
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'accounts:logout' %}">로그아웃</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'accounts:update' %}">회원 정보 수정</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'accounts:change_password' %}">비밀 번호 수정</a>
              </li>
            {% else %}
              <li class="nav-item">
                <a class="nav-link" href="{% url 'accounts:signup' %}">회원가입</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'accounts:login' %}">로그인</a>
              </li>
            {% endif %}
          </ul>
        </div>
      </div>
    </nav>
    <div class="container mt-5">

      {% block content %}{% endblock content %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    {% bootstrap_javascript %}
  </body>
</html>
```

bootstrap에서 nav바를 끌어다 사용하였고. `{% if request.user.is_authenticated %}{% else %}{% endif %}`를 사용하여 로그인 된 상태와 로그아웃 상태에서 네브바를 다르게 보이도록 설정하였습니다. 



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





# 정리 해보니 궁금해진 것들

1. 정리를 하면서 보니까 request.user 가 로그인을 한 과정에서 나온거 같은데 어떤 원리에 의해 html에서도 사용할 수 있는지 잘 모르겠습니다. + request.user.delete()이게 왜 작동이 되는지를 모르겠습니다. 
2. modelForm은 주로 새롭게 DB를 만들거나 수정할때 주로 사용하고, Form은 인증할때 주로 사용하는거 같은데. 비밀번호를 관리하는 폼만 이상하게 Form을 사용하는거 같은데. 제가 잘못 추측한 건지 아니면 비밀번호는 특별해서 그런건지 알고 싶습니다. 



# 프로젝트를 해서 좋았던 점

프로젝트 할때 마다 느끼는 거지만 혼자서 공부 할 때 보다 사람들이랑 같이 내 생각을 말해보고 상대방 이야기를 들어보고 할때가 기억에 잘 남는거 같습니다. 그리고 내가 아는 것을 설명해 보면서 내가 대략적으로 아는것에서 내가 어디를 제대로 알고 있고 어디를 모르고 있는지를 파악할 수 있어서 좋았습니다. 그리고 이러한 경험은 더 큰 동기부여로 다가오는거 같습니다. 



# 정리 해 보고 느낌점

개인적으로 지난주 보다 이번주에 배운것이 많이 어렵다고 느꼈는데 막상 정리해 보니까 생각보다 별거는 없었던거 같습니다. 다만, 그 구조가 너무 낯설어서 이것저것 만지면서 그 구조를 대략적으로 이해하고 글로 정리하는데 많은 시간이 소요되었던거 같습니다. (15시간 걸렸습니다ㅠㅠ)

정리를 한다고 했는데. 제가 봐도 복잡한 설명이 많네요ㅠ 



















