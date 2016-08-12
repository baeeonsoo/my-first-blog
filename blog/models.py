from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')     #다른 모델에 대한 링크를 의미
    title = models.CharField(max_length=200)    #글자 수가 제한된 텍스트
    text = models.TextField()                   #글자 수 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(        #날짜와 시간을 의미
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
