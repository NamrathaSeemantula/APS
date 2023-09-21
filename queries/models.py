from django.db import models

# Create your models here.

class queries(models.Model):
    query = models.CharField(max_length = 2000) 
    author = models.CharField(max_length = 100, default = "")
    tag = models.CharField(max_length = 100, default = "")
    
    def __str__(self):
        return self.query   

class answers(models.Model):
    query = models.ForeignKey(queries, related_name = "comments", on_delete = models.CASCADE)
    answerauthor = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 3000)

    def __str__(self):
        return '%s - %s' %(self.query.query, self.answerauthor)
