from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^notice/',include('notices.urls',namespace='notices')),
    url(r'^resources/',include('resources.urls',namespace='resources')),
    url(r'^attendance/',include('attendance_proxy.urls',namespace='attendance')),
)
