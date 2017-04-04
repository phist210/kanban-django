from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    priority = models.IntegerField()
<<<<<<< HEAD
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)
=======
    owner = models.ForeignKey('auth.User', related_name='task',
                              on_delete=models.CASCADE)
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed
