from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 유지 모델을 참조하는 경우
    # 방법1. (권장하지 않음)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 방법2. (권장) settings.AUTH_USER_MODEL == 'accounts.User'
    # user = models.ForeignKey(setting.AUTH_USER_MODEL, ondelete=models.CASCADE)
    # 방법3. (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # comment_set = 쟝고가 자동으로 추가해주는 칼럼
    # user_id = 쟝고가 자동으로 추가해주는 칼럼

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 쟝고가 자동으로 추가해주는 칼럼
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user+id = 쟝고가 자동으로 추가해주는 칼럼