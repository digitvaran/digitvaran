from django.conf.urls import patterns,include,url
from resources import views

urlpatterns=patterns('',
    url(r'^$',views.home,name='home'),
    url(r'^search/$',views.search,name='search'),
    
)
