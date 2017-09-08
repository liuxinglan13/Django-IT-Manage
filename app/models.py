from django.db import models
from django.urls import reverse
# Create your models here.


# 主机的分类

class HostCategorys(models.Model):
    category = models.CharField(max_length=70)

    def __str__(self):
        return self.category


# 主机的分组（所在资源池）
class HostGroups(models.Model):
    group = models.CharField(max_length=70)

    def __str__(self):
        return self.group


# 操作系统分类

class OperatingSystems(models.Model):
    operatingsystem = models.CharField(max_length=30)

    def __str__(self):
        return self.operatingsystem


# 主机的使用状态（在用，停用，等）
class Host_status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status

class Host(models.Model):
    # IP地址
    ip = models.CharField(max_length=20)
    # 主机名
    host_name = models.CharField(max_length=50)
    # 主机的用途,可以为空
    host_purpose = models.CharField(max_length=100, blank=True)
    # 主机的使用状态 和 Host_status 对应
    host_status = models.ForeignKey(Host_status)
    # 主机的分类，和 HostCateorys 一对一
    Host_category = models.ForeignKey(HostCategorys)
    # 主机的所属组，和HostGroups 一对一
    Host_group = models.ForeignKey(HostGroups)
    # 主机的操作系统类型
    Host_operatingsystem = models.ForeignKey(OperatingSystems)
    # 管理员账号
    admin_Account = models.CharField(max_length=50, blank=True)
    # 管理员密码
    admin_password = models.CharField(max_length=50, blank=True)
    # 主机的详细信息备注
    Host_body = models.TextField(max_length=1000, blank=True)
    # 创建和最后一次修改时间
    # auto_now_add 自动保存当前时间 进数据
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # 这个方法用来生产url
    def get_absolute_url(self):
        return reverse('app:host_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.host_name
