from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.host_edit, name='host_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.HostDetailView.as_view(), name='host_detail'),
    url(r'^new/$', views.host_new, name='host_new'),
]
