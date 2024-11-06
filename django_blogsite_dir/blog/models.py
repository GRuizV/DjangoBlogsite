from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(verbose_name="content")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 'on_delete=models.CASCADE' means 'if an user is deleted, all its post too'

    def __str__(self):
        return self.title
    
    # Blog Detail Url

    def get_absolute_url(self):
        return reverse("blog-detail",args=[self.title])


