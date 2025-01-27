from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    cover = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title