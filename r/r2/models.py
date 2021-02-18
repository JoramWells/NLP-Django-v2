from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
#from ckeditor.fields import RichTextField

class PostQ(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name='blog', blank=True,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    body=models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('quote-detail')



    
class Post(models.Model):
    keyword = models.CharField(max_length=255)
    min_videos = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
