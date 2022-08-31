from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.TextField()
    contents = models.TextField()
    photo = models.ImageField(blank=True, upload_to='board/post/%Y/%m/%d')
    author = models.TextField()
    is_public = models.BooleanField(default=True, verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title