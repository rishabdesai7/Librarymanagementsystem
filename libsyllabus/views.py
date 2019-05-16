from django.shortcuts import render
from libadmin.views import home,Luser
from django.contrib.auth.models import User
from .models import Syllabus,Textbooks
# Create your views here.

try:
    def syllabus(req, con={}):
        if req.user.is_authenticated:
            con.update({'mail':req.user.username})
            return render(req, 'libsyllabus/syllabus.html',con)
        return home(req)


    def getsyllabus(req):
        try:
            sem = req.GET.get('sem')
            k = User.objects.get(username=req.user.username)
            k = Luser.objects.get(username=k)
            s = Syllabus.objects.get(dept=k.dept, sem=sem)
            tb = (Textbooks.objects.all().filter(dept=k.dept, sem=sem))
            return syllabus(req,{'link': s.syllabus.url,'show':s.syllabus,'link1':s.coursefile.url,'show1':s.coursefile,'tb': tb,'mail':k.username})
        except:
            return syllabus(req)
finally:
    pass