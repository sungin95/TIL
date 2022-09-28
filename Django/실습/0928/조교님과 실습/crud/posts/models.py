from email.policy import default
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 80)
    # defalut : 데이터를 생성할 때 값을 안넣으면 자동으로 값을 채워서 데이터를 생성하겠다. 
    completed = models.BooleanField(default=False)
    