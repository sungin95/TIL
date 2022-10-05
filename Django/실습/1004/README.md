# 오늘배운거 다시 되새기기



python -m venv venv

. venv/script/activate

pip list

pip install django=3.2.13

pip install black

django-admin startproject a_pjt .

python manage.py startapp articles

앱 등록

pjt urls.py include("articles.urls")

articles urls.py 생성후 view.py 수입(연결), 앱이름 생성, index 페이지 생성

view에서 index 함수 생성

models.py 생성후 class 생성. 이름은 Articles

index함수는 render을 사용하고 Articles의 모든 데이터를 모두 보내주는 형태로 작성

index.html은 해당 변수를 받고 for을 사용하여 사용자에게 모두 보여준다. 



여기까지 기본 세팅을 하면 create를 만들어 보자

{% csrf_token %} {{ article_form.as_p }}를 사용할것이다. 

우선 forms.py를 만들어 준다. 그리고 

forms.py

기존에는 form의 input에 name을 붙여서 이 name을 바탕으로 view.py에서 Request.GET.get("title")이렇게 하나하나 만들어서 이걸로 create를 만들어서 관리를 했는데. 이제는 편하게 아래 코드만 사용하여 관리를 할 수 있게 되었는데.  **fields = ["title", "content"]** 확인해 본 결과 순서에 의해 관리가 되는건 아니고 아마 model 안의 변수와 이름을 비교하고, 어떤 타입인지를 바탕으로 자동 생성되는 원리인거 같다. 

```python
from django import forms # 수입
from .models import Article # 사용할 모델


class ArticleForm(forms.ModelForm): # 새롭게 이름을 지어주고, "forms.ModelForm"를 쳐 준다. 
    class Meta: # 이건 외워야 겠지??
        model = Article # 내가 사용하려는 모델
        fields = ["title", "content"] # all을 사용하는 방법도 있고 title, content를 지정해 주는 방법도 있다. 
```

앗 이것을 만들기 전에 models.py에서 먼저 클래스와 속성을 설정을 해 줘야 한다. 



여기까지 하면 오늘 배운 새로운 장고의 기능 사용할 준비를 끝 마쳤다. 이제 적용을 하면 된다. 

장고가 지원해 주는 기능은 

1. html에서 input을 대신 만들어 주고 

2. view.py에서 request값을 새로만든 `ArticleForm` 을 사용한다. 

   - get일때는 request값을 사용하지 않는다. (이걸 사용하기 전에는 get일때는 관련해서 만들어 주기도 않았다. )

   - post일때는 `request.POST` 를 인자로 넣어준다. 

     - get은 조회이고 post는 값 추가 or 삭제등 과정이므로 값을 바꾸기 위해 request로 입력된 값을 받는다. 
     - ArticleForm(request.POST)만 하면 끝나는 과정이라 매우 편하다. 

   - 나쁜 사용자들이 있어서 보안에 문제가 생길 수 있으니까 장고에서 제공하는 보안프로그램을 이용하자. 간단하다.  

     `변수 = ArticleForm(request.POST)`를 .is_valid()메서드를 이용하여 체크를 하면 된다. 이 값이 True가 나오면 save()를 해서 값을 저장하면 된다. 

     False가 나오면 통과 시키지 말고 그 값을 보내주면 장고가 알아서 메시지까지 보내준다. 

 

이제 urls.py에서 create 경로를 설정해 준 다음

views.py에서 create함수를 만들고 이 함수를 조회(get)를 목적으로 들리면 ArticleForm()로(빈 request) 해당 페이지로 render을 시켜 주고 값 변경(post)을 목적으로 들어오면 위 규칙에 맞게 변경시킨후 redirect를 시켜준다. 

이것으로 새로 목록 만들기 페이지 들어가기 와 새로운 페이지 만들기 둘이 끝났다. 

이제 만든 페이지 수정 페이지 들어가기와 해당 페이지 수정하기 둘이 남았다. 

html부분은 반복이 되고 주소창 들어가는 부분도 지난번에 했으므로 생략하겠다. 

그래서 view부분을 설명하자면 아까 만든거랑 똑같은데. 2가지가 다르다. 

1. 함수 인자로 request뿐 아니라 pk도 받는다. 

   pk처럼 예전처럼 Article.objects.get(pk=pk)식으로  pk값을 통해 해당 정보를 불러온다. 

2. 그 정보를 instance=변수명 으로 넣어준다. 그러면 이 새로운 식에서 이 값을 인식한다. 











