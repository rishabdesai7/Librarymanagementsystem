from django.contrib import admin

# Register your models here.
from .models import Syllabus,Textbooks
admin.site.register(Syllabus)
admin.site.register(Textbooks)
