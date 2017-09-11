from ..models import Host, HostCategorys, HostGroups, Host_status
from django import template
from django.db.models.aggregates import Count

register = template.Library()


# 获取所有主机组 自定义标签
@register.simple_tag
def get_group():
    return HostGroups.objects.annotate(num_posts=Count('host')).filter(num_posts__gt=0)


# 获取所有主机状态
@register.simple_tag
def get_status():
    return Host_status.objects.annotate(num_posts=Count('host')).filter(num_posts__gt=0)


# 获取主机分类  生产/测试/虚拟机/物理机
@register.simple_tag
def get_categorys():
    return HostCategorys.objects.annotate(num_posts=Count('host')).filter(num_posts__gt=0)