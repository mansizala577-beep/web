from django.db import models

# Create your models here.


class mansi(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(default="noemail@example.com")


class car(models.Model):
    car_name=models.CharField(max_length=50)
    speed=models.IntegerField(default=50)

    def __str__(self)->str:
        return self.car_name
    


