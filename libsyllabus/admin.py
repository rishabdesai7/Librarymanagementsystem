from django.contrib import admin

# Register your models here.
from .models import Syllabus,Textbooks,Subject
admin.site.register(Syllabus)
admin.site.register(Textbooks)
admin.site.register(Subject)

