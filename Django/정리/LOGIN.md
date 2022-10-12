# LOGIN

## 로그인에 대한 이해

HTTP특징

- 비 연결 지향(connectionless) 
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
    - 예를 들어 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님 
    - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
  - 무상태(stateless) 
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음 
    - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적
- 어떻게 로그인 상태를 유지할까?
  - 그런데 우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 “상태”가 유지됨
  - 서버와 클라이언트 간 지속적인 상태 유지를 위해 “쿠키와 세션”이 존재

[참고]실시간 방송은 HTTP이 아니라 다른 프로토콜이다. 



## 쿠키란?

예시 쿠팡

장바구니에 담은것을 쿠키를 지우면 사라진다. (네트워크 탭에서 확인 가능)

쿠키는 한국으로 치면 마패와 같은 것이다. 암행어사가 문제가 되는 것을 찾는데 임금님과 계속 통신을 할 수가 없다. 하지만 본인의 역할을 수행해야 하므로 마패증을 받아서 수행을 합니다. 그것처럼 클라이언트에서 서버로 계속해서 요청을 보내면 비용도 많이 들고 느려질 수 밖에 없다 이 문제를 해결하기 위해 서버는 응답으로 쿠키를 하나 생성해 주고 이 쿠키가 있는 동안에 해당 작업을 지속 상태로 있게 해 준다. 



시크릿 모드가 쿠키가 없는 상태로

## 쿠키 사용 목적

- 세션 관리 (Session management)
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리 
- 개인화 (Personalization) 
  - 사용자 선호, 테마 등의 설정 
- 트래킹 (Tracking) 
  - 사용자 행동을 기록 및 분석



### 세션

- 사이트와 특정 브라우저 사이의 state(상태) 를 유지시키는 것 
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장 
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달 
  - 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 알맞은 로직을 처리 
- session id 는 세션을 구별하기 위해 필요하며, 쿠키에는 session id 만 저장



## 쿠키와 세션 차이

- 쿠키와 세션은 비슷한 역할을 하며, 동작원리도 비슷합니다. 그 이유는 세션도 결국 쿠키를 사용하기 때문입니다.
- 가장 큰 차이점은 사용자의 정보가 저장되는 위치입니다. 때문에 쿠키는 서버의 자원을 전혀 사용하지 않으며, 세션은 서버의 자원을 사용합니다.
- 보안 면에서 세션이 더 우수하며, 요청 속도는 쿠키가 세션보다 더 빠릅니다. 그 이유는 세션은 서버의 처리가 필요하기 때문입니다.
- 보안, 쿠키는 클라이언트 로컬에 저장되기 때문에 변질되거나 request에서 스니핑 당할 우려가 있어서 보안에 취약하지만 세션은 쿠키를 이용해서 sessionid 만 저장하고 그것으로 구분해서 서버에서 처리하기 때문에 비교적 보안성이 좋습니다.
- 라이프 사이클, 쿠키도 만료시간이 있지만 파일로 저장되기 때문에 브라우저를 종료해도 계속해서 정보가 남아 있을 수 있다. 또한 만료기간을 넉넉하게 잡아두면 쿠키삭제를 할 때 까지 유지될 수도 있습니다.
  - Persistent cookies
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨
- 반면에 세션도 만료시간을 정할 수 있지만 브라우저가 종료되면 만료시간에 상관없이 삭제됩니다. 예를 들어, 크롬에서 다른 탭을 사용해도 세션을 공유됩니다. 다른 브라우저를 사용하게 되면 다른 세션을 사용할 수 있습니다.
  - Session cookie
    - 현재 세션(current session)이 종료되면 삭제됨 
    - 브라우저 종료와 함께 세션이 삭제됨
- 속도, 쿠키에 정보가 있기 때문에 서버에 요청시 속도가 빠르고 세션은 정보가 서버에 있기 때문에 처리가 요구되어 비교적 느린 속도를 가집니다.

## 쿠키/세션은 캐시와 엄연히 다르다!

- 캐시는 이미지나 css, js파일 등을 브라우저나 서버 앞 단에 저장해놓고 사용하는 것입니다.
- 한번 캐시에 저장되면 브라우저를 참고하기 때문에 서버에서 변경이 되어도 사용자는 변경되지 않게 보일 수 있는데 이런 부분을 캐시를 지워주거나 서버에서 클라이언트로 응답을 보낼 때 header에 캐시 만료시간을 명시하는 방법등을 이용할 수 있습니다.
- 보통 쿠키와 세션의 차이를 물어볼 때 저장위치와 보안에 대해서는 잘 말하는데 사실 중요한 것은 라이프사이클을 얘기하는 것입니다.



장고 admin 로그인 

데이터 베이스에 저장

django session_key

settings



django.contrib.sessions 세션 관리

MIDDLEWARE

사이에 처리해야 하는 것들을 처리 해줌

인증과 검토 절차

요청과 응답을 처리할때 사용

## Session in Django

- Django는 database-backed sessions 저장 방식을 기본 값으로 사용 
  - session 정보는 Django DB의 django_session 테이블에 저장 
  - 설정을 통해 다른 저장방식으로 변경 가능 
    - https://docs.djangoproject.com/en/3.2/topics/http/sessions/ 
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 확인함



# 사용방법

## AuthenticationForm

- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력 받음(username, password) 
  - ModelForm이 아닌 일반 Form을 상속 받고 있으며, request를 첫번째 인자로 취함

```python
# accounts/urls.py
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
	path('login/', views.login, name='login'),
]
```

```html
<!-- accounts/login.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>로그인</h1>
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
    	pass
    else:
    	form = AuthenticationForm()
    context = {
    	'form': form
    }
    return render(request, 'accounts/login.html', context)
```



## login()

- login(request, user, backend=None) 
- 인증된 사용자를 로그인 
  - 유저의 ID를 세션에 저장하여 세션을 기록 
- HttpRequest 객체와 User 객체가 필요 
  - 유저 정보는 반드시 인증된 유저 정보여야 함 
    - authenticate()함수를 활용한 인증 
    - AuthenticationForm을 활용한 is_valid

 ### 로직 작성

- 일반적인 ModelForm 기반의 Create 로직과 동일하지만, 
  - ModelForm이 아닌 **Form**으로 필수 인자 구성이 다름 
  - DB에 저장하는 것 대신 세션에 유저를 기록하는 함수 호출함(login() 함수) 
    - View 함수와 이름이 동일하여 변경하여 호출 
    - 로그인 URL이 ‘/accounts/login/’에서 변경되는 경우 settings.py LOGIN_URL을 변경하여야 함

```python
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
    	form = AuthenticationForm()
    context = {
    	'form': form
    }
    return render(request, 'accounts/login.html', context)
```

### get_user()

- AuthenticationForm의 인스턴스 메서드 
- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
- https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L244

### 세션 데이터 확인

#### DB

- 로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션 확인 (로그인은 관리자 계정을 만든 후 진행) 
- django_session 테이블에서 확인

#### 브라우저

- 브라우저에서 확인 개발자도구 – Application - Cookies



## Authentication with User

`{{ user }}`

login: username

logout: AnonymousUser

#### html 에서 확인

`if request.user.is_authenticated`

## 로그인 기능

- URL: GET/accounts/login
- 처리:
  - 사용자에게 Form을 제공한다. 
- URL: POST/accounts/login/
- 처리:
  - (로그인) 로직처리
    - 사용자인지, 확인하고,django_session 테이블에 저장, 쿠키 주기
  - (성공) 게시글 목록 페이지로 redirect
  - (실패) 로그인 Form



## logout()

- logout(request) 
- 요청 유저에 대한 세션 정보를 삭제함 
  - DB에서 session data 삭제
  - 클라이언트의 쿠키에서 sessionid 삭제 
- HttpRequest 객체를 인자로 받고 반환 값이 없음 
- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

## 사용 방법

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

```python
# accounts/views.py

from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

```python
<!-- base.html -->

<body>
    <div class="container">
        <h3>Hello, {{ user }}</h3>
        <a href="{% url 'accounts:login' %}">Login</a>
        <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}	
            <input type="submit" value="Logout">
        </form>
        <hr>
        {% block content %}
        {% endblock content %}
    </div>
</body>
```



## is_authenticated

- User model의 속성(attributes) 중 하나 
- 사용자가 인증 되었는지 여부를 알 수 있는 방법 
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성 
- AnonymousUser에 대해서는 항상 False 
- 일반적으로 request.user에서 이 속성을 사용 (`request.user.is_authenticated`) 
- 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

```html
로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기
<!-- base.html -->

{% if request.user.is_authenticated %} <!-- 여기 -->
    <h3>Hello, {{ user }}</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
    </form>
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
    <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
    </form>
{% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```

```python
View에서의 처리도 반드시 필요함
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

## login_required

```python
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    pass

@login_required
def delete(request, pk):
	pass

@login_required
def update(request, pk):
	pass
```

### next 대응

```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
    	return redirect('articles:index')
    
    if request.method == 'POST':
    	form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
```

### next 주의 사항

- 만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않음 
- 해당 action 주소 next 파라미터가 작성 되어있는 현재 url이 아닌 /accounts/login/ 으로 요청을 보내기 때문

```python
<!-- accounts/login.html -->

{% block content %}
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST"> <!-- {% url 'accounts:login' %}가 잘못 되었다.  -->
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
{% endblock content %}
```



## 참고

- Django Auth 기본
  - https://docs.djangoproject.com/en/4.1/topics/auth/default/
- Django User Model
  - https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
- Custominzing
  - https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
- 비밀번호 암호화
  - https://docs.djangoproject.com/en/3.2/topics/auth/passwords/
  - https://d2.naver.com/helloworld/318732













