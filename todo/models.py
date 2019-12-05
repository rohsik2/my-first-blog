from django.db import models
from django.utils import timezone

# Create your models here.
class Bucket(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    fin_date = models.DateTimeField(blank=True, null = True)
    is_fin = models.BooleanField(default=True)
    
    def finish(self):
        self.fin_date = timezone.now()
        self.is_fin = True
        self.save()
    
    def __str__(self):
        return self.title
        