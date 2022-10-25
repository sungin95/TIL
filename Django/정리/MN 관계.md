# M:N 관계

## 새롭게 등장하는 개념

`models.ManyToManyField()`

메서드 종류 • add(), remove(), create(), clear(), set() 등

## 2개의 models.ForeignKey()

2개의 ForeignKey를 사용하여 나타낼 수 있다. 

```python
class Patient(models.Model):
	name = models.TextField()
    
	def __str__(self):
		return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
    	return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

하지만 이렇게 하면 가능은 한데 불편하다는 느낌이 강한거 같다. 

## models.ManyToManyField()

```python
# hospitals/models.py

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    
    def __str__(self):
    	return f'{self.pk}번 환자 {self.name}’
    
# Reservation Class 주석 처리
```

```python
# 이렇게 생성을 하였다면
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

```python
# 이렇게 활용할 수 있다. 
# 환자 -> 의사

# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>]>
```

```python
# 의사 -> 환자

# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)

# doctor1 - 자신의 예약 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

# patient1, 2 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

patient2.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>
```

### 삭제

```python
# doctor1이 patient1 진료 예약 취소

doctor1.patient_set.remove(patient1)

doctor1.patient_set.all()
<QuerySet [<Patient: 2번 환자 harry>]>

patient1.doctors.all()
<QuerySet []>

# patient2가 doctor1 진료 예약 취소

patient2.doctors.remove(doctor1)

patient2.doctors.all()
<QuerySet []>

doctor1.patient_set.all()
<QuerySet []>
```



### 역참조 이름 바꾸기

```python
class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
    
    def __str__(self):
    	return f'{self.pk}번 환자 {self.name}'
```

```python
# 1번 의사 조회하기
doctor1 = Doctor.objects.get(pk=1)

# 에러 발생 (related_name 을 설정하면 기존 _set manager는 사용할 수 없음)
doctor1.patient_set.all()
AttributeError:'Doctor' object has no attribute 'patient_set'

# 변경 후
doctor1.patients.all()
<QuerySet []>
```



### through 정보 연동시키기

- 그렇다면 중개 모델을 직접 작성하는 경우는 없을까? 
  - 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음 
- 가장 일반적인 용도는 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우
- through 설정 및 Reservation Class 수정 
  - 이제는 예약 정보에 증상과 예약일이라는 추가 데이터가 생김

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()
    
    def __str__(self):
    	return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    	return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```



### symmetrical (feat. self)

- 기본 값 : True 
- ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용

```python
# 예시

class Person(models.Model):
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)
```

- symmetrical 
  - True일 경우 
    - _set 매니저를 추가 하지 않음 
    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭) 
    - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨 
  - 대칭을 원하지 않는 경우 False로 설정 
    - Follow 기능 구현에서 다시 확인할 예정

### 유저를 받는 변수 두개를 만들었더니 오류가 생겼다(feat. 좋아요)

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```
$ python manage.py makemigrations
ERRORS:
articles.Article.like_users: (fields.E304) Reverse accessor for 'Article.like_users' clashes with
reverse accessor for 'Article.user'.
	HINT: Add or change a related_name argument to the definition for 'Article.like_users' or
'Article.user'.
articles.Article.user: (fields.E304) Reverse accessor for 'Article.user' clashes with reverse
accessor for 'Article.like_users'.
	HINT: Add or change a related_name argument to the definition for 'Article.user' or
'Article.like_users'.
```

문제의 원인은 `user.article_set`을 했을때 기준을 `user`를 할지 `like_users`을 할지를 알 수가 없게 됨.

이 문제를 해결하기 위해 `related_name="like_articles"`를 사용한다. 

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 좋아요 구현

url

```python
# articles/urls.py

urlpatterns = [
	...
	path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

views

```python
# articles/views.py
def likes(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	if article.like_users.filter(pk=request.user.pk).exists():
    	# if request.user in article.like_users.all():
    	article.like_users.remove(request.user)
    else:
    	article.like_users.add(request.user)
    return redirect('articles:index')
```

exits()란?

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환 
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

html

```html
<!-- articles/index.html -->
{% extends 'base.html' %}
{% block content %}
    …
    {% for article in articles %}
        …
        <div>
            <form action="{% url 'articles:likes' article.pk %}" method="POST">
                {% csrf_token %}
                {% if request.user in article.like_users.all %}
                	<input type="submit" value="좋아요 취소">
                {% else %}
                	<input type="submit" value="좋아요">
                {% endif %}
            </form>
        </div>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
    {% endfor %}
{% endblock content %}
```





