from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'georeal_web'

urlpatterns = [
    path('', views.home, name='home'),
    path('cookies', views.cookies, name='cookies'),
]

urlpatterns += staticfiles_urlpatterns()