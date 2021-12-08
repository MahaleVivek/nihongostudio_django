from django.db import models

# Create your models here.
class main(models.Model):
    blog = models.CharField(max_length=200)

    def __str__(self):
        return f" {self.blog} "


