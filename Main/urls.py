from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.home, name='Main-main'),
    url('^about/$', views.about, name='Main-about'),
]
