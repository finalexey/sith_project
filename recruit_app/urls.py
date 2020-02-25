from django.urls import path
from . import views
#from django.conf.urls import url, include


urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('forsith', views.forsith, name='forsith'),
    path('forrecr', views.forrecr, name='forrecr'),
]
