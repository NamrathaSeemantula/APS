from django.db import models

# Create your models here.

class events(models.Model):
    eventTopic = models.CharField(max_length=300, default="")
    eventDesc = models.CharField(max_length=3000, default="")
    eventImg = models.ImageField(upload_to = 'event_pics', blank = True)
    eventDate = models.CharField(max_length=50, default="")
    eventOrganizer = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.eventTopic