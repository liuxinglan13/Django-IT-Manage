from ..models import Host, HostCategorys, HostGroups, Host_status
from django import template

register = template.Library()

# 获取所有主机组
@register.simple_tag
def get_tag():
    return HostGroups.objects.all()