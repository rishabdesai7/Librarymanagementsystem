from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login,name = 'login'),
    path('sdash',views.dashboard,name = 'sdash'),
    path('changepwd',views.changepwd,name = 'changepwd'),
    path('auth',views.auth,name = 'authenticate'),
    path('logout',views.logout,name = 'logout'),
    path('feedback',views.feedback,name = 'feedback'),
    path('books',views.books,name = 'books'),
    path('cron',views.cron,name = 'cron'),
    path('renew/<str:bid>/',views.renew,name = 'renew'),
    path('activate',views.activate,name = 'activate'),
    path('activation/<str:id>/', views.activation, name='activation'),
]
