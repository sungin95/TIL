# 장고 SQL

우선 가상환경을 깔아 주고 실행한다. 

python -m venv venv

. venv/scripts/activate

문서에 있는 내용을 설치 한다. 

pip install -r requirements.txt

서버 실행, 장고 sql 시작하기.

python manage.py runserver
python manage.py shell_plus



# 문법

```
Post.objects.all()
Post.objects.create(author=me, title='Sample title', text='Test')
User.objects.get(username='ola')
Post.objects.filter(author=me)
Todo.objects.order_by('id')
Todo.objects.filter(priority=5).order_by('id')
Todo.objects.filter(priority=5).count()
A = Todo.objects.get(id=1)
A.delete()
exit()
```

## DateField

`수정일자 : auto_now=True 사용`

`생성일자 : auto_now_add=True 사용`