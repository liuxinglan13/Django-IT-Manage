from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.HostEditView.as_view(), name='host_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.HostDetailView.as_view(), name='host_detail'),
    url(r'^new/$', views.HostCreateView.as_view(), name='host_new'),
    url(r'^hostgroup/(?P<pk>[0-9]+)/$', views.HostGroupView.as_view(), name='host_group'),

]
