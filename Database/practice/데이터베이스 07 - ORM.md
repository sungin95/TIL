# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
>

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name            | debut      | country |
| --------------- | ---------- | ------- |
| 봉준호          | 1993-01-01 | KOR     |
| 김한민          | 1999-01-01 | KOR     |
| 최동훈          | 2004-01-01 | KOR     |
| 이정재          | 2022-01-01 | KOR     |
| 이경규          | 1992-01-01 | KOR     |
| 한재림          | 2005-01-01 | KOR     |
| Joseph Kosinski | 1999-01-01 | KOR     |
| 김철수          | 2022-01-01 | KOR     |

> 코드 작성
>

```python
In [8]: Director.objects.create(name = "봉준호", debuf= "1993-01-01", country="KOR")
Out[8]: <Director: Director object (1)>

In [12]: Director.objects.create(name = "김한민", debuf= "1999-01-01", country="KOR")
Out[12]: <Director: Director object (2)>

In [13]: Director.objects.create(name = "최동훈", debuf= "2004-01-01", country="KOR")
Out[13]: <Director: Director object (3)>

In [14]: Director.objects.create(name = "이정재", debuf= "2022-01-01", country="KOR")
Out[14]: <Director: Director object (4)>

In [15]: Director.objects.create(name = "이경규", debuf= "1992-01-01", country="KOR")
Out[15]: <Director: Director object (5)>

In [16]: Director.objects.create(name = "한재림", debuf= "2005-01-01", country="KOR")
Out[16]: <Director: Director object (6)>

In [17]: Director.objects.create(name = "Joseph Kosinki", debuf= "1999-01-01", country="KOR")
Out[17]: <Director: Director object (7)>

In [18]: Director.objects.create(name = "김철수", debuf= "2022-01-01", country="KOR")
Out[18]: <Director: Director object (8)>

In [19]: Director.objects.all()
Out[19]: <QuerySet [<Director: Director object (1)>, <Director: Director object (2)>, <Director: Director object (3)>, <Director: Director object (4)>, <Director: Director object (5)>, <Director: Director object (6)>, <Director: Director object (7)>, <Director: Director object (8)>]>

```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title  |
| ------ |
| 액션   |
| 드라마 |
| 사극   |
| 범죄   |
| 스릴러 |
| SF     |
| 무협   |
| 첩보   |
| 재난   |

> 코드 작성
>

```python
In [21]: Genre.objects.create(title="액션")
Out[21]: <Genre: Genre object (1)>

In [23]: Genre.objects.create(title="드라마")
Out[23]: <Genre: Genre object (2)>

In [24]: Genre.objects.create(title="사극")
Out[24]: <Genre: Genre object (3)>

In [25]: Genre.objects.create(title="범죄")
Out[25]: <Genre: Genre object (4)>

In [26]: Genre.objects.create(title="스릴러")
Out[26]: <Genre: Genre object (5)>

In [27]: Genre.objects.create(title="SF")
Out[27]: <Genre: Genre object (6)>

In [28]: Genre.objects.create(title="무협")
Out[28]: <Genre: Genre object (7)>

In [29]: Genre.objects.create(title="첩보")
Out[29]: <Genre: Genre object (8)>

In [30]: Genre.objects.create(title="재난")
Out[30]: <Genre: Genre object (9)>
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
>

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
>

```python
directors = Director.objects.all()
for director in directors:
     print(director.name,director.debuf,director.country)
#봉준호 1993-01-01 00:00:00 KOR
#김한민 1999-01-01 00:00:00 KOR
#최동훈 2004-01-01 00:00:00 KOR
#이정재 2022-01-01 00:00:00 KOR
#이경규 1992-01-01 00:00:00 KOR
#한재림 2005-01-01 00:00:00 KOR
#Joseph Kosinki 1999-01-01 00:00:00 KOR
#김철수 2022-01-01 00:00:00 KOR
#진짜 겨우 찾았네요
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
>

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
>

```python
director = Director.objects.get(id=1)
print(director.name, director.debuf, director.country)
#봉준호 1993-01-01 00:00:00 KOR
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
>

```python
Director.objects.get(country = "USA")
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
>

```bash
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
Input In [51], in <cell line: 1>()
----> 1 Director.objects.get(country = "USA")

File ~\OneDrive\바탕 화면\수업자료 당겨오기\ORD 실습\DB-ORM-master\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     84 def manager_method(self, *args, **kwargs):
---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~\OneDrive\바탕 화면\수업자료 당겨오기\ORD 실습\DB-ORM-master\venv\lib\site-packages\django\db\models\query.py:496, in QuerySet.get(self, *args, **kwargs)
    494     return clone._result_cache[0]
    495 if not num:
--> 496     raise self.model.DoesNotExist(
    497         "%s matching query does not exist." % self.model._meta.object_name
    498     )
    499 raise self.model.MultipleObjectsReturned(
    500     "get() returned more than one %s -- it returned %s!"
    501     % (
   (...)
    504     )
    505 )

DoesNotExist: Director matching query does not exist.
```

> 이유 작성
>

```
get은 하나의 값만을 출력하는데. 이때 값이 중복되거나 없으면 오류를 발생한다. 그래서 주로 id을 찾을 때 사용하고, 이런 상황을 위해서 id가 아니면 보통 filter을 사용한다. 
# DoesNotExist: Director matching query does not exist.(실제 오류 메시지)
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
>

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
>

```python
dire = Director.objects.filter(name="Joseph Kosinki")
for d in dire:
    d.country = "USA"
for d in dire:
    d.save()
dire = Director.objects.filter(country = "USA")
for d in dire:
    print(d.name, d.debuf, d.country)
# Joseph Kosinki 1999-01-01 00:00:00 USA # 입력할때 실수로 이름 철자 하나가 틀립니다. 
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
>

```python
Director.objects.get(country = "KOR")
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
>

```bash
---------------------------------------------------------------------------
MultipleObjectsReturned                   Traceback (most recent call last)
Input In [108], in <cell line: 1>()
----> 1 Director.objects.get(country = "KOR")

File ~\OneDrive\바탕 화면\수업자료 당겨오기\ORD 실습\DB-ORM-master\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
     84 def manager_method(self, *args, **kwargs):
---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~\OneDrive\바탕 화면\수업자료 당겨오기\ORD 실습\DB-ORM-master\venv\lib\site-packages\django\db\models\query.py:499, in QuerySet.get(self, *args, **kwargs)
    495 if not num:
    496     raise self.model.DoesNotExist(
    497         "%s matching query does not exist." % self.model._meta.object_name
    498     )
--> 499 raise self.model.MultipleObjectsReturned(
    500     "get() returned more than one %s -- it returned %s!"
    501     % (
    502         self.model._meta.object_name,
    503         num if not limit or num < limit else "more than %s" % (limit - 1),
    504     )
    505 )

MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
>

```
get의 값은 반드시 하나여야 한다. 구지 비유를 하자면 한가지 음식이 담여야 하는 그릇입니다. 그런데 여기에 7가지 음식을 넣을려고 하니 넘치기 전에 미리 경고의 메시지를 우리에게 주는 것입니다. 
이런 상황에서는 음식이 있든 없든, 몇개가 있든 신경을 안쓰는 filter라는 그릇에 담아줘야 더 적절할 것입니다. 
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
>

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
>

```python
dire = Director.objects.filter(country = "KOR")
for d in dire:
	print(d.name, d.debuf, d.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get과 filter는 땅과 하늘 입니다. 
get는 땅으로 땅은 모두 지구를 통해 이어져 있기 때문에 1개입니다. 
filter 하늘입니다. 하늘은 대기권, 성층권, 우주 등으로 나누어져 있다고도 말 할 수 있지만 그저 공간일뿐 실체가 없기 때문에 없다고도 말 할 수 있기 때문입니다. 
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
>

```python
dire = Director.objects.get(name = "김철수")
dire.delete()
# (1, {'db.Director': 1})
```