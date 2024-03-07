from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import CustomUser_Model
class Post(models.Model):

    MY_CHOICES = {
        'Private':'Private',
        'Public': 'Public'
    }
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes')
    category = models.CharField(max_length=100, default='null')
    visibility = models.CharField(max_length=20, choices=MY_CHOICES, default='public')
    
    # Add more fields as needed
    
    class Meta:
        ordering = ['-created_date']  # Orders posts by most recent first

    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
