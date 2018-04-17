from django.conf.urls import url, include
from . import views

app_name = "calendario"

urlpatterns = [ 
                url(r'^$', views.viewCalendar, name='viewCalendar'),                     
            ]