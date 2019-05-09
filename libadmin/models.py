from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dept(models.Model):
    '''
    This db stores all departments
    '''
    dept = models.CharField(max_length=5)
    def __str__(self):
        return self.dept
class Luser(models.Model):
    '''
    This db stores details about students
    '''
    uid = models.CharField(max_length=10,primary_key=True)
    dept = models.ForeignKey(to=Dept,on_delete= models.CASCADE)
    username = models.ForeignKey(to=User,on_delete=models.CASCADE)
    isactivated = models.BooleanField(default=False)
    def __str__(self):
        return self.uid
class Book(models.Model):
    '''
    This db holds book details
    '''

    bid = models.CharField(max_length= 10,primary_key=True)
    name = models.CharField(max_length= 100)
    author = models.CharField(max_length= 100)
    issue = models.CharField(max_length=1,default= 'N')
    idate = models.DateField(null= True,blank=True)
    uid = models.ForeignKey(to=Luser,on_delete = models.DO_NOTHING,null = True,blank=True)
    rdate = models.DateField(null=True,blank=True)
    rcount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

