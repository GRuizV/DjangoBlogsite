from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.


# Comments Model

class Comments(models.Model):
    user = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,verbose_name='Post',on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Message')
    confirm = models.BooleanField(default=False,verbose_name="Confirm and display on the site")

    def __str__(self) :
        return (self.message)