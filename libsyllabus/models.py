from django.db import models
from libadmin.models import Dept
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
# Create your models here.
class Subject(models.Model):
    '''
    This database holds subjects
    '''
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.subject
class Textbooks(models.Model):
    '''
    This database holds Tb data per subject
    '''
    dept = models.ForeignKey(to=Dept,on_delete=models.CASCADE)
    sem = models.IntegerField()
    subject = models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    textbook = models.CharField(max_length=100)
    ebooks = models.CharField(max_length= 1500,null=True,blank=True)
    def __str__(self):
        return self.subject
    class Meta:
        unique_together = (('dept', 'sem','subject'),)

class Syllabus(models.Model):
    '''
    This database holds syllabus
    '''
    dept = models.ForeignKey(to=Dept,on_delete=models.CASCADE)
    sem = models.IntegerField()
    syllabus = models.FileField(null=True,upload_to='docs',storage=gd_storage)
    coursefile = models.FileField(null=True,upload_to='docs', storage=gd_storage)
    def __str__(self):
        return str(self.dept) + str(self.sem)
    class Meta:
        unique_together = (('dept', 'sem'),)

