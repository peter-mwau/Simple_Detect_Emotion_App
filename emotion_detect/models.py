from django.db import models

# Create your models here.

class Records_log(models.Model):
    Query = models.CharField(max_length=100)
    Emotion = models.CharField(max_length=100)
    Time = models.DateTimeField(auto_now_add=True)

    
