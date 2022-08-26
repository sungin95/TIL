객체

파이썬의 모든것

객체는 속성과 메서드를 가지고 있다. 

타입이기도 하다. 

클래스 인스턴스

사람 아이유 지민

틀 사례

속성 & 메서드

속성: 값 , 메서드 함수



# ORM

우리들이 파이썬으로 데이터베이스를 조작하는 것. 



## ORM이란

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크 에서는 내장 Django ORM을 활용

장고 맛보기간 될 거 같다. (신기하다 정도의 느낌만 있어도 OK)

시스템 간의 데이터 변환 기술 



파이썬으로 데이터 베이스를 조작한다

“객체(object)로 DB를 조작한다.”

Genre.objects.all()

# 가상환경 설정

```$ python -m venv venv```

```$ source venv/Scripts/activate```

```$ pip list```   (체크)

```$ python manage.py shell_plus```

```$ deactivate``` (종료)



* pip install
```bash
pip install -r requirements.txt 
# requirements.txt 
appnope==0.1.3
asgiref==3.5.2
asttokens==2.0.8
backcall==0.2.0
click==8.1.3
decorator==5.1.1
Django==4.0.6
django-extensions==3.2.0
executing==0.10.0
ipython==8.4.0
jedi==0.18.1
matplotlib-inline==0.1.6
mypy-extensions==0.4.3
parso==0.8.3
pathspec==0.9.0
pexpect==4.8.0
pickleshare==0.7.5
platformdirs==2.5.2
prompt-toolkit==3.0.30
ptyprocess==0.7.0
pure-eval==0.2.2
Pygments==2.13.0
six==1.16.0
sqlparse==0.4.2
stack-data==0.4.0
tomli==2.0.1
traitlets==5.3.0
typing_extensions==4.3.0
wcwidth==0.2.5
```

* django 패키지 설치 확인
```bash
python manage.py --version
# 4.0.6
```

## 모델 마이그레이션

```bash
# 마이그레이션과 migrate는 터미널에서 반드시 실행 해주세요. 
# 우선 생성한 테이블과 타입을 class의 형식으로 만들어 줍니다. 
python manage.py makemigrations
python manage.py migrate
# 그 다음 위 두 식 실행하면 적용된 파일이 생성됩니다. 
python manage.py shell_plus
# 그리고 이 식을 입력하면 sqlite3와 비슷한 상태가 됩니다. 
# 이 공간에서 파이썬 사용이 가능합니다. 
# 나갈떄는 exit()
```

```bash
# ORM 활용시 파이썬 코드는 shell에서 반드시 실행 해주세요.
python manage.py shell_plus 
IN [1] : Genre.objects.all()
```

**### 파일 실행**

| 파일을 실행할 때에는 가상환경을 실행한 상태인지 꼭 확인합니다.

```bash
python main.py
```

## CRUD

• Create

```python
# 1. create 메서드 활용
Genre.objects.create(name='발라드')
# 2. 인스턴스 조작
genre = Genre()
genre.name = '인디밴드'
genre.save()
```

• Read

```python
# 1. 전체 데이터 조회
Genre.objects.all()
# <QuerySet [<Genre: Genre object (1)>, <Genre:
Genre object (2)>]>
# 2. 일부 데이터 조회(get)
Genre.objects.get(id=1)
# <Genre: Genre object (1)>
# 3. 일부 데이터 조회(filter)
Genre.objects.filter(id=1)
# <QuerySet [<Genre: Genre object (1)>]>
```

• Update

```python
# 1. genre 객체 활용
genre = Genre.objects.get(id=1)
# 2. genre 객체 속성 변경
genre.name = '트로트’
# 3. genre 객체 저장
genre.save()
```

• Delete

```python
# 1. genre 객체 활용
genre = Genre.objects.get(id=1)
# 2. genre 객체 삭제
genre.delete()
```

## get & filter

```
get과 filter는 땅과 하늘 입니다. 
get는 땅으로 땅은 모두 지구를 통해 이어져 있기 때문에 1개입니다. 
filter 하늘입니다. 하늘은 대기권, 성층권, 우주 등으로 나누어져 있다고도 말 할 수 있지만 그저 공간일뿐 실체가 없기 때문에 없다고도 말 할 수 있기 때문입니다. 
get은 언제나 하나 입니다. 그래서 주로 고유값은 id를 검색 할 때 쓰입니다. (없으면 오류가 떠 바로 알 수 있고, 중복되어도 바로 알 수 있습니다. )
filter는 0 ~ 무한 입니다. 그래서 리스트로 저장이 되고 값을 불러올때 몇번째 값인지 지정을 안 해 주면 나오지 않습니다. 
```

fiilter().values 를 하면 디셔너리화 가능하다. 





# QuerySet API

API: 기능, 코드로 뭘 하겠거니 하면 이해가 쉽다.





```
(id__gt=4)
(id__gte=4)
(id__lt=4)
(id__lte=4)
(id__in=[1,3,4])
(headline__in = "abc")
(headline__startswich = "lennon")
(headline__istartswich = "lennon")
```

장점: 많은 부분을 DB에서 알아서 핸들링 해준다

단점: 세세한 설정, 데이터 조작이 어렵다?



```python
# range
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
```

복합 활용

```python
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=inner_qs)
```

활용

```
Entry.objects.all()[0]
Entry.objects.order_by('id')
Entry.objects.order_by('id')
Entry.objects.order_by(‘-id')
```







print(Genre.objects.get(id=1).query)

오류

개별 인스턴스를 반환하니까

# ORM 확장

## 모델링

```python
class Genre(models.Model):
	name = models.CharField(max_length=30)
class Artist(models.Model):
	name = models.CharField(max_length=30)
	debut = models.DateField()
class Album(models.Model):
	name = models.CharField(max_length=30)
	genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
	artist = models.ForeignKey('Artist',on_delete=models.CASCADE)
```

• Foreign Key (외래키) 

​	• 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성) 

​	• 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성 

​	• 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

models.ForeignKey 필드 

​	• 2개의 필수 위치 인자 

​		• Model class : 참조하는 모델 

​		• on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식 

​			• CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제

​			 • PROTECT : 삭제되지 않음 

​			 • SET_NULL : NULL 설정 

​			• SET_DEFAULT : 기본 값 설정

```python
artist = Artist.objects.get(id=1)
genre = Genre.objects.get(id=1)
album = Album()
album.name = '앨범1'
album.artist = artist # 1. 객체의 저장
album.genre = genre
album.save()
```

```python
class Genre(models.Model):
	name = models.CharField(max_length=30)
class Artist(models.Model):
	name = models.CharField(max_length=30)
	debut = models.DateField()
class Album(models.Model):
	name = models.CharField(max_length=30)
	genre = models.ForeignKey('Genre’,on_delete=models.CASCADE)
	artist = models.ForeignKey('Artist’,on_delete=models.CASCADE)
```

```python
# 1. 참조
album = Album.objects.get(id=1)
album.artist
# <Artist: Artist object (1)>
album.genre
# <Genre: Genre object (1)>
# 2. 역참조
genre = Genre.objects.get(id=1)
genre.album_set.all()
# <QuerySet [<Album: Album object (1)>, <Album:
Album object (2)>]>
```



```python 
genre = Genre.obects.get(id=1)
genre.album_set.all()
# album의 ㅇ인스턴스가 담긴 쿼리셋. 1:N
# 트로트인 앨범들 쿼리셋
# 앨범의 장르 인스턴스
```

