from django.db import models

# Create your models here.
class Comment(models.Model):

    textOfComment = models.CharField(max_length=200,)
    userName = models.CharField(max_length=20,)

    
