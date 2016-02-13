from django.conf import settings
from django.conf.urls import patterns, url
from rizr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users_api/', views.UserList.as_view()),
    url(r'^users_api/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    )
    
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )