from django.contrib import admin
from .models import  Dept,Luser,Book
# Register your models here.
admin.site.register(Dept)
admin.site.register(Luser)
admin.site.register(Book)