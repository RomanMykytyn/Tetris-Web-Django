from django.db import models

# Create your models here.
class Comment(models.Model):

    textOfComment = models.CharField(max_length=200,)
    userName = models.CharField(max_length=20,)

class userScore(models.Model):
    userName = models.CharField(max_length=20,)
    score = models.CharField(max_length=50,)
    totalScore = models.IntegerField(default=0)
