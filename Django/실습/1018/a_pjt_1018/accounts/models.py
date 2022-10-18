from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    pass


class profile(models.Model):
    profile_image = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )
    content = models.TextField()
    article = models.ForeignKey(User, on_delete=models.CASCADE)
