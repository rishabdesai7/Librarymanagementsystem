from django.urls import path

from . import views

urlpatterns = [
    path('',views.syllabus, name='syllabus'),
    path('populate',views.getsyllabus,name = 'getsyllabus')
]