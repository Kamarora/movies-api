from django.db import models

# class Roles(models.Model):  
#     rid = models.AutoField(primary_key=True)
#     rname = models.CharField(max_length=100)  
#     class Meta:  
#         db_table = "roles"

class Users(models.Model):  
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    upassword = models.CharField(max_length=100)  
    uemail = models.EmailField()  
    ucontact = models.CharField(max_length=15)
    role = models.CharField(max_length=1, choices=(('A', 'Admin'),('U', 'User')))
    class Meta:  
        db_table = "users"  

class Movies(models.Model):  
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=100)  
    mactor = models.CharField(max_length=255)
    mactress = models.CharField(max_length=255)
    mdirector = models.CharField(max_length=255)
    msummary = models.TextField(null=True,blank=True)
    class Meta:  
        db_table = "movies"