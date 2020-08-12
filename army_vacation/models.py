from django.db import models

# Create your models here.


class Vacation(models.Model):
    SORT_OF_VACATIONS = (
        ('YG', '연가'),
        ('PS', '포상휴가'),
        ('WR', '위로휴가'),
        ('CW', '청원휴가'),
        )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
