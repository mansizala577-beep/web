from django.db import models

# Create your models here.


class Receipe (models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="receipes/")


class tcp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15, default='0000000000')
    message = models.TextField()



class userroy(models.Model):
    usrname = models.CharField(max_length=100)
    usrEmail = models.EmailField(default="noemail@example.com")
    usrcontect = models.IntegerField(default=0)  # default added
    usrpassword = models.CharField(max_length=50, default='Default Value')
    usrstates = models.BooleanField(default=True)


class ptnsmasten(models.Model):
    pasname=models.CharField(max_length=100)   
    pascontact=models.EmailField()
    pasaddress=models.CharField()
    pascity=models.CharField()
    pasStatus=models.BooleanField(default=True)    



class userps(models.Model):
    Usrname = models.CharField(max_length=100)
    UsrEmaile = models.EmailField() 
    UsrPassword = models.CharField(max_length=100)



   