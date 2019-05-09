from django.db import models
from libadmin.models import Dept
# Create your models here.

class Textbooks(models.Model):
    '''
    This database holds Tb data per subject
    '''
    dept = models.ForeignKey(to=Dept,on_delete=models.CASCADE)
    sem = models.IntegerField()
    subject = models.CharField(max_length=100)
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
    syllabus = models.FileField()
    def __str__(self):
        return str(self.dept) + str(self.sem)
    class Meta:
        unique_together = (('dept', 'sem'),)
