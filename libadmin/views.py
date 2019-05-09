from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as l
from django.contrib.auth import logout as o
from django.contrib.auth.models import User
from .models import Luser,Book
import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode as de
from django.utils.http import urlsafe_base64_encode as en

def sendmail(r, msg):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    k = server.starttls()
    k = server.login('bookelakha@gmail.com', 'book@1234')
    k = server.sendmail(from_addr='bookelakha@gmail.com',to_addrs=[r],msg = msg)




# Create your views here.
def home(req):
    return render(req, 'libadmin/home.html')


def login(request, msg=''):
    return render(request, 'libadmin/login.html', {'message': msg})


def changepwd(req):
    return render(req, 'libadmin/changepwd.html')


def auth(request):
    id, pwd = request.POST['id'], request.POST['password']
    u = authenticate(username=id, password=pwd)
    if u:
        l(request, u)
        return dashboard(request)
    return login(request, 'Invalid Credentails')


def dashboard(request):
    if request.user.is_authenticated:
        k = User.objects.get(username=request.user.username)
        try:
            k = Luser.objects.get(username=k)
        except Exception:
            return login(request,'Invalid Credentails')
        content = {
            'id': k.uid,
            'dept': k.dept,
            'mail': k.username,
            'isactivated': k.isactivated
        }
        return render(request, 'libadmin/sdash.html', content)
    return login(request, 'Invalid Credentails')


def logout(request):
    o(request)
    return home(request)


def feedback(req):
    return render(req, 'libadmin/Feedback.html')


def books(request):
    if request.user.is_authenticated:
        k = User.objects.get(username=request.user.username)
        k = Luser.objects.get(username=k)
        b = list(Book.objects.all().filter(uid=k.uid))
        return render(request, 'libadmin/books.html', {'books': b, 'mail': k.username})


def cron(req):
    d = datetime.date.today() + datetime.timedelta(days=1)
    books = list(Book.objects.all())
    for x in books:
        if x.rdate == d:
            sendmail(x.uid.username.username, "hey dude ! please renew " + x.name)
    return HttpResponse(content=200)


def renew(req, bid):
    try:
        b = Book.objects.get(bid=bid)
        if b.rcount >= 2:
            raise Exception
        else:
            b.idate, b.rdate, b.rcount = datetime.date.today(), datetime.date.today() + datetime.timedelta(days=15), b.rcount + 1
            b.save()
            messages.success(req,'Successfully Renewed!')
            return books(req)
    except Exception:
        messages.error(req,'Online renewal limit exceeded ! Go for Physical Renewal :)')
        return books(req)


def activate(req):
    from email.mime.text import MIMEText
    email = en(bytes(req.user.username.encode('UTF8'))).decode('UTF8')
    msg = req.build_absolute_uri()[:-1] + 'ion/'+email
    msg = 'hey dude , this is your activation link ' + msg
    msg = MIMEText(msg, _charset="UTF-8")
    sendmail(req.user.username,msg.as_string())
    return logout(req)

def activation(req,id):
    id = de(id).decode('UTF8')
    u = Luser.objects.get(username = User.objects.get(username = id))
    u.isactivated = True
    u.save()
    res = '<html>' \
          '<body body bgcolor="azure">' \
          '<h2 align = "center" >Congratulations your account is activated , <br> to login ' \
          '<a href = "/libadmin/login">click here</a>' \
          '</h2>' \
          '</body>' \
          '</html'
    return HttpResponse(res)


