from django.db import models
from accounts.models import UserProfileInfo
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class blogs(models.Model):
    blogtopic = models.CharField(max_length = 200)
    blogcontent = models.CharField(max_length = 3000)
    

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1) 
    author = models.CharField(max_length = 100, default = "")
    tag = models.CharField(max_length = 100, default = "")
    
    def __str__(self):
        return self.blogtopic   

class blogcomments(models.Model):
    blog = models.ForeignKey(blogs, related_name = "comments", on_delete = models.CASCADE)
    commentauthor = models.CharField(max_length = 200)
    commentcontent = models.CharField(max_length = 3000)

    def __str__(self):
        return '%s - %s' %(self.blog.blogtopic, self.commentauthor)
