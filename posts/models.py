from django.db import models

# Create your models here.

class posts(models.Model):
    postimage = models.ImageField(upload_to = 'posts_pics', blank = True)
    caption = models.CharField(max_length=1000, default="")
    author = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.author

class postcomments(models.Model):
    post = models.ForeignKey(posts, related_name = "comments", on_delete = models.CASCADE)
    commentauthor = models.CharField(max_length = 200)
    commentcontent = models.CharField(max_length = 3000)

    def __str__(self):
        return self.commentauthor