from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    """ 게시판 글 모델 클래스 """
    # 제목
    title = models.CharField(max_length=250)
    # 내용
    content = models.TextField()
    # 작성자
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
    )
    tag = models.CharField(max_length=30)

