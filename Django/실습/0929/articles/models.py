from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=80)
