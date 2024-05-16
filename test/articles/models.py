from django.db import models
from django.conf import settings

class Article(models.Model):
   # on_delete=models.SET_NULL 사용자를 지워도 포스트는 삭제되지 않고 null로 남음, 이때 null=True를 해야 오류가 안남
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
   like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_article')      # 게시글 좋아요 누른 사람
   title = models.CharField(max_length=20)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
   # 대댓글 역참조 
   parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
   content = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)