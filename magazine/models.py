from django.db import models
from django.urls import reverse

# Create your models here.

#model for the posts
class Post(models.Model):
    the_text = models.CharField(max_length=150)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, default=1)
    body = models.TextField(default=' ')

    #to display characters instead of objects
    def __str__(self):
        return self.the_text

    def get_absolute_url(self):
        return reverse('home')