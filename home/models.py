from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='blog_images')

    def __str__(self) :
        return self.title