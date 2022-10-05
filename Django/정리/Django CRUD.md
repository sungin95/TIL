# Django CRUD



pip freeze > requirements.txt

가상환경 만들기 



URL 요청 보냄 

서버에 들어감

URL목록이 나오고 해당 함수를 실행, 함수는 render를 함

이렇게 정리하면 맞겠죠?

요청(form:get or post, a: 주소창) -> 처리(url에 맞는 함수 실행) -> 응답(render or redirect)



python manage.py showmigrattions



그냥 post를 사용하면 오류가 뜬다. 

데이터 베이스에서 자료를 받지 못했다. 

post는 / ?title=??? 식으로 기록 되지 않는다. 

get은 조회일 수 밖에 없다

로그인, 회원가입은 post를 사용한다.



프레인워크 풀패키지 프렌차이즈랑 같다



# Django ModelForm

html 서버 둘다 처리해야 한다

이유 사고(html은 바꾸기가 쉽다. )



서버에 required주는 법

forms.py(일반적으로 이 이름 사용)

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        or
        fields = ['title','content']
추가적인 작업은 문서를 통해서
```

값을 넘겨주고 싶다? content

views.py

```python
def new(request):
    article_form = ArticleForm()
    context = {
        "article_form": article_form
    }
    
형식 파괴
def create(request):
    article_form = ArticleForm(request.POST)
    if article_form.is_valid():
        article_form.save()
    else:
        print("유효하지 않습니다.....!!")
        
    return redirect('articles:index')
```



index.html (자동으로 만들기 까지 해줌)

```html
{% csrf_token %}
{{ article_form.as_p }}
```





이전글 가져요기

{{ article_form.as_p }}



이제는 실제 값을 바꾸는 과정이 필요하다.



instance=article 이걸 계속 해 주어야 한다. 







