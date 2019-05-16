from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

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
    issued = models.BooleanField(default = False)
    idate = models.DateField(null= True,blank=True)
    uid = models.ForeignKey(to=Luser,on_delete = models.DO_NOTHING,null = True,blank=True)
    rdate = models.DateField(null=True,blank=True)
    rcount = models.PositiveIntegerField(default=0)
    fine= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class BookAdmin(admin.ModelAdmin):
    model = Book
    readonly_fields = ['rdate','idate','fine','rcount']


@receiver(post_save, sender = Book, dispatch_uid="set_dates")
def set_dates(sender,instance,**kwargs):
    if not instance:
        return
    if hasattr(instance,'_recurpre'):
        return
    if instance.issued:
        instance.idate = datetime.date.today()
        instance.rdate = datetime.date.today() + datetime.timedelta(days=15)
        instance.fine = 0
        instance.rcount = 0
    try:
        instance._recurpre=True
        instance.save()
    finally:
        del instance._recurpre








'''
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()


class Map(models.Model):
    id = models.AutoField( primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='docs', storage=gd_storage)


'''



