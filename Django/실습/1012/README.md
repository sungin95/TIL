## 목표

Django Auth를 활용한 회원관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)가 가능한 서비스를 개발합니다.

## 요구사항

### 모델 Model

- 모델 이름 : User
  
    Django **AbstractUser** 모델 상속
    

### **폼 Form**

회원가입

- Django 내장 회원가입 폼 UserCreationForm을 상속받아서 **CustomUserCreationForm** 생성
  
    해당 폼은 아래 필드만 출력
    
    - username
    - email
    - password1
    - password2

로그인

- Django 내장 로그인 폼 **AuthenticationForm** 활용

### 기능  View

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- **CustomUserCreationForm**을 활용해서 회원가입 구현

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

### 화면 Template

메인 페이지 

- `GET` http://127.0.0.1:8000/
- 회원가입 페이지 이동 버튼
- 회원 목록 페이지 이동 버튼
- 로그인 상태에 따라 다른 화면 출력
    - 로그인 상태
        - 로그인 한 사용자의 username 출력
            - username 클릭 시 해당 회원 조회 페이지(프로필 페이지)로 이동
        - 로그아웃 버튼
    - 비 로그인 상태
        - 로그인 페이지 이동 버튼
        - 회원가입 페이지 이동 버튼

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 테이블
- 회원 아이디를 클릭하면 해당 회원 조회 페이지(프로필 페이지)로 이동

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼


# 처음 세팅 
pip install (django==3.2.13, black, bootstrap5 )
base.html 만들기 

-    settings.TEMPLATES  "DIRS": [BASE_DIR / "templates"],

static 만들기

- settings

  ```python
  STATIC_URL = "/static/"
  STATICFILES_DIRS = [
      BASE_DIR / "static",
      "/var/www/static/",
  ]
  ```

  ```html
  {% load static %}
  {% static 'css/style.css' %}
  ```

AUTH_USER_MODEL = "accounts.User"



# 만드는 과정

우선 어제 했던 회원가입 과정을 반복해야 했다. 

회원가입을 하기 위해서는 

modelForm을 활용해 view함수를 if,else구문을 이용해 만든것과 똑같은 함수를 만들면 되는데. 한 가지가 다르다. 







nslookup www.google.com

tracert www.google.com
