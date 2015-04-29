from django.conf.urls import patterns, include, url
from attendance_proxy import views
urlpatterns = patterns('',
    url(r'^$', views.home,name='home'),
    url(r'^(?P<prog>\d+)/(?P<sem>\d+)/(?P<mm>\d+)/$', views.attendance,name='attendance'),
)
