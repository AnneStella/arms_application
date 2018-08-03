from django.conf.urls import url
from .import views

app_name = 'my_app'

urlpatterns = [

    url(r'^apply/', views.apply, name='apply'),
 ]
