from django.db import models

# Create your models here.
class FreeLancer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    followers = models.IntegerField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name