# DRF(정리하면서 공부)

## 사용하는 이유

### **Rest full**

예전만해도 웹 페이지를 보여주는 웹서버만 구현하면 됐다. 그 웹 서버에서 DB 서버의 데이터도 읽어오고 사용자들이 글을 남기면 DB 서버에 저장까지 하는 기능을 모두 담당했다. 하지만 스마트폰이 나오고, 어플리케이션의 등장으로 더이상 웹으로만 서비스를 제공하는 것에는 한계가 있었다.

따라서 HTML로 렌더링 하는 웹서버가 아닌, JSON 혹은 XML 과 같은 형식을 통해서 데이터를 다루는 별도의 API 서버가 필요했다.
스마트폰 어플과 웹에서 동일한 기능을 제공하는데 기존의 웹서버를 계속 사용하면 매번 HTML을 읽어서 해당 태그에 있는 정보를 찾아내는 일은 매우 힘들고 비효율적이다

따라서 RESTful 기능을 HTT MetPhod와 함께 사용해 웹, 데스크탑 앱, 스마트폰 어플들까지 하나의 API 서버를 생성할 수 있다.



### **DRF**

DRF(Django Rest Framework)란Django 안에서 RESTful API 서버를 쉽게 만들게 도와주는 라이브러리다.



# 사용방법

우선 `pip install djangorestframework`



그리고 실제 장고 서버와 REST 서버는 따로 운영이 되어야 합니다.

`python manage.py startapp todo_subject_restful_main`



settings.py 에서

`rest_framework`,

`todo_subject_restful_main`,

두 개를 등록해 줍니다. 



그럼 여기에 serializers.py가 있다. 

이걸 통해 데이터를 통신할 수 있게 된다. 



미리 모델을 만들어 주고

serializers.py에 등록한다. 

```python
from .models import TodoList
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')
```



그리고 다시 모델로 가서 

```python 
from django.db import models

class TodoList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)
    ...
```

db_column='NO' 이런식으로 해야 하는거 같다.



그리고 views.py로 가서

모델과 serializers와 rest_framework를 상속시켜 준다. 

```python
from .models import TodoList
from .serializers import TodoSerializer
from rest_framework import viewsets

class Todo_subject_restful_main(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
```







