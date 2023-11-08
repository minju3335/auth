from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # article_set = 자동으로 추가된 칼럼
    # comment_set = 자동으로 추가된 칼럼