from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^hostlist/$', views.HostView.as_view(), name='host'),
    url(r'^host/(?P<pk>[0-9]+)/edit/$', views.HostEditView.as_view(), name='host_edit'),
    url(r'^host/(?P<pk>[0-9]+)/$', views.HostDetailView.as_view(), name='host_detail'),
    url(r'^new/$', views.HostCreateView.as_view(), name='host_new'),
    url(r'^host/(?P<id>[a-z]+)/(?P<pk>[0-9]+)/$', views.HostFilterView.as_view(), name='host_filter'),

]
