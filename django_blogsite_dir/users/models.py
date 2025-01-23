from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpeg',
        upload_to='profile_pics',
        storage=S3Boto3Storage() if not settings.DEBUG else None )  # Gate to storage depending if in Debuggin mode or Production


    def __str__(self):
        return f'{self.user.username} Profile'


    # Commented Out to allow AWS S3 to save images
    # def save(self, *args, **kwargs): # This function was overridden to resize large images
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)





