from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.f
import mysite.settings as settings
class Vacation(models.Model):
    SORT_OF_VACATIONS = (
        ('YG', '연가'),
        ('PS', '포상휴가'),
        ('WR', '위로휴가'),
        ('CW', '청원휴가'),
        )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.CharField(
        max_length=2,
        choices=SORT_OF_VACATIONS,
        default='YG',)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Menu(models.Model):
    date = models.DateField()
    breakfast = models.TextField()
    lunch  = models.TextField()
    dinner = models.TextField()

class Worker(models.Model):
    date = models.DateField()
    carde = models.TextField()
    day_soldier = models.TextField()
    night_soldier = models.TextField()


    