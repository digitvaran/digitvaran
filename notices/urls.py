from django.conf.urls import patterns, include, url
from notices import views
urlpatterns = patterns('',
    url(r'^$', views.home,name='home'),
    url(r'^(?P<delta>\d+)/$',views.timeperiod,name='timeperiod_view'),
    url(r'^success/$',views.success_save,name='successful_save'),
    url(r'^new/$',views.new_notice,name='new'),
)
