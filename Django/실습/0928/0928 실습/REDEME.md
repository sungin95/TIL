# 만든과정 되새겨 보기

가상환경 폴더를 만들고 실행한다. 

python -m venv venv

. venv/scripts/active

pip list 로 확인후 장고를 설치하고 프로젝트 폴더 생성.

pip install django==3.2.13

pip install black 도 같이 설치

django-admin startproject [project_name] .

python manage.py runserver 로 확인 후 앱 폴더 만들기

python manage.py startapp [app_name] 

이제 settings를 통하여 앱을 등록해 주고(INSTALLED_ APP) 

TEMPLATES 에서 'DIR' 에서 [BASE_DIR / "templates"]를 해주고 가장 바깔에(프로젝트안에 말고 프로젝트랑 같은 위치)templates를 생성하고 base.html를 설치해 준다. (현재 상황에서는 필요는 없지만 실제 개발이라는 가정하여 만들어 준다. )

base.html 는 {% block content %} {% endblock %}을 사용하여 이 안 부분을 제외하고 공유하는 부분을 만들어 준다. 공유하는 부분을 다 넣어주자!(부트스트랩도 넣어주자!)

앱폴더에 ulrs.py생성

프로젝트의 urls 에서 include를 사용하여 앱에서 주소창을 관리(이것 역시 현재 필요는 없지만 구지 만들어 보자!!!)

이때 include() 괄호 안에 "앱이름.urls"로 만들어 준다. 

이제 앱의 urls에서 주소창을 관리해 주고 앱 주소창 이름을 정해주자. (app_name = "todos")

또한 주소창을 적을때도 이름을 적어 주어 변수화를 하자!(path("", views.index, name="index"),)

이제 path랑 views를 불러오자!



## request vs redirect

request: 매번 변화하는 값이 아니라 이어지는 값이다. 그래서 모든 render에는 request가 있다. 그러니까 request는 어떠한 틀이고 이 안에 값은 바뀌고 이게 다음으로 이어지고. 

request는 form의 input의 name으로 값을 추가(수정) 할 수 있고 이 값들을 저장 함으로써 다음에 활용하게 해야 하는데. 그것이 render(request,....)과정이라고 생각한다.

redirect: 재귀함수랑 비슷한 역할이라고 본다. 값을 바꾸고 다른 함수를 작동시킨다. 여기에서 create, delete는 request의 값만 바꾸고 index를 다시 실행시키고 request값은 그 상태에서 저장이 된다. 

## get vs post

get은 URL과 끝에 파라미터를 포함하여 전송이 된다. `www.example.com/login?id=hyoin&password=123456`

post는 내용을 HTTP의 body에 담아서 전송한다. get보다는 보안에 강하지만 별도의 작업을 하지 않으면 간단한 툴로도 내용을 확인 할 수 있다. 

(다음 교육 받을때 post를 어떤것을 추가 해서 보안을 강화하는지 중점으로 공부해야 할거 같다. )

## 파라미터란?(아직 잘 모르겠...)

매개 변수

URL파라미터

URL 중에서 물음표 ‘?’ 이후 문자열

[파라미터 명]=[파라미터 값]이 한 세트

‘&’로 이어줍니다.

## form vs a

form 사용자에게 입력받은 값을 전달

a 그냥 보내 준다. 

이 문제에서는 

{% for todo in todos %}

todo.pk

{% endfor %}

를 사용하여 a태그에 해당 숫자 링크를 달아서 문제를 해결 했다. 

## index.html

path("", views.index, name="index"),를 생성 

view.py에도 index함수를 만들어 준다. 그리고 앱폴더에 templates 폴더를 생성하고 앱 이름과 같은 폴더를 추가 생성하고 그 안에 index.html을 만들어 준다.(폴더 추가 생성 이유는 필요는 없지만 실전과 비슷한 상황을 연출하기 위해 구지 해 주자!)

- index함수:
  - index.html에서 입력한 값을 create로 보내고 데이터베이스에 저장된 모든 내용을 보여주는 역할을 할 예정이다. 
  - 데이터 베이스 내용을 all()을 사용하여 변수화 해서 보내준다. 
  - 이 페이지는 보여주는 곳이므로 return 값으로 render을 사용하고 앱이름:index.html을 렌더링 하고 데이터 베이스 내용을 변수화 하여 보내준다. 
- index.html 
  - form을 통해 input한 내용을 데이터 베이스로 저장을 해야 한다. 
  - 그러기 위해 form 과 input을 만들고 input에 name을 준다.(name값을 이용하여 views.py에서 request.GET.get("name이름")을 통하여 갖고 올 수 있다. )
  - input을 하나의 form으로 묶어 주고 각 input에는 적절한 type를 줘서 원하는 정보를 수집할 수 있는 형태로 바꾸어 준다. 그리고 정보의 최대 길이등의 옵션을 추가 설정해 준다. 마지막으로 type="submit"를 통하여 클릭하면 해당 정보가 form통해 전달이 되게 한다. 

## create

- 받은 내용을 데이터베이스에 저장후에 다시 index.html로 돌아간다. 
- index함수에서는 입력한 값을 request로 받고 각 input의 name을 통하여 정보를 구분하여 변수로 만들어준다. 
- 변수를 바탕으로 새롭게 class이름.objects.create()을 활용하여 데이터 값을 추가 해 준다. 
- redirect를 사용하여 index함수를 다시 실행해 준다. 

## 데이터베이스 구축

- 데이터 베이스에 저장하기 위해 models.py에서 class를 만들어 준다. 그후 

  - python manage.py makemigration

  - python manage.py migrate

  를 사용하여 데이터 베이스를 등록해 준다. 

## delete

삭제를 할때 필요한건 내가 삭제 하고자 하는 글의 id(pk)이다. 

a태그에는 delete주소창 + 해당 id로 태그가 달려 있다. 

url은 path("delete/<int:todo_pk>", views.delete, name="delete"),이렇게 적었고

그러면 클릭하면 delete함수에 (request,todo_pk) 두개의 인자가 보내지게 되고 

delete함수에서는 todo_pk를 통하여 해당 오브젝트를 찾아주어 변수화를 한다. 

clicked_id = Todo.objects.get(pk=todo_pk)

이 변수를 삭제하면 끝

clicked_id.delete() (delete가 바로 데이터 베이스에 영향을 준다. 아마도...)

여기서 redirect redirect("todos:index")를 하여 

path("", views.index, name="index"),를 다시 실행하여 준다. 

## modify

delete랑 비슷하다. 

우선 pk값을 통해 불러온 값을 내가 원하는 값으로 바꾸어 주고

delete대신 save를 써 주면 된다. 





복습 끝~!!!