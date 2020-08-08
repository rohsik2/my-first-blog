from django.db import models

# Create your models here.


class Vacation(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
