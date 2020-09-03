from django.db import models
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

    def __str__(self):
        return str(self.date)

class Worker(models.Model):
    date = models.DateField()
    carde = models.TextField()
    day_soldier = models.TextField()
    night_soldier = models.TextField()

class WashWorker(models.Model):
    date = models.DateTimeField()
    time = models.CharField(max_length=10)
    soldier1 = models.CharField(max_length=10)
    soldier2 = models.CharField(max_length=10)
    soldier3 = models.CharField(max_length=10)
    soldier4 = models.CharField(max_length=10)
    def __str__(self):
        return str(self.date + self.time)

class NightWorker(models.Model):
    date = models.DateField()
    carde = models.CharField(max_length=10)
    soldier1 = models.CharField(max_length=10)
    soldier2 = models.CharField(max_length=10)
    soldier3 = models.CharField(max_length=10)
    soldier4 = models.CharField(max_length=10)
    soldier5 = models.CharField(max_length=10)
    def __str__(self):
        return str(self.date)