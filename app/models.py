from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


# 主机的分类

class HostCategorys(models.Model):
    name = models.CharField(max_length=70, verbose_name='主机分类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "主机分类"
        verbose_name_plural = verbose_name


# 主机的分组（所在资源池）
class HostGroups(models.Model):
    name = models.CharField(max_length=70, verbose_name='主机属组名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "主机属组"
        verbose_name_plural = verbose_name

# 操作系统分类

class OperatingSystems(models.Model):
    name = models.CharField(max_length=30, verbose_name='主机操作系统')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "主机操作系统"
        verbose_name_plural = verbose_name

# 主机的使用状态（在用，停用，等）
class Host_status(models.Model):
    name = models.CharField(max_length=10, verbose_name='主机状态')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "主机状态"
        verbose_name_plural = verbose_name

# 主机的种类（物理机，虚拟机）

class Host(models.Model):
    # IP地址
    ip = models.GenericIPAddressField(verbose_name="IP地址", max_length=20)
    # 主机名
    host_name = models.CharField(max_length=20, verbose_name='主机名')
    # 主机的用途,可以为空
    host_purpose = models.CharField(max_length=20, blank=True, verbose_name='用途')
    # 主机的使用状态 和 Host_status 对应
    host_status = models.ForeignKey(Host_status, verbose_name='状态')
    # 主机的分类，和 HostCateorys 一对一
    Host_category = models.ForeignKey(HostCategorys, verbose_name='分类')
    # 主机的所属组，和HostGroups 一对一
    Host_group = models.ForeignKey(HostGroups, verbose_name='属组')
    # 主机的操作系统类型
    Host_operatingsystem = models.ForeignKey(OperatingSystems, verbose_name='操作系统')
    # 管理员账号
    admin_Account = models.CharField(max_length=20, blank=True, verbose_name='管理员账号')
    # 管理员密码
    admin_password = models.CharField(max_length=20, blank=True, verbose_name='管理员密码')
    # 主机的详细信息备注
    Host_body = RichTextUploadingField(blank=True, verbose_name='备注')
    # 创建和最后一次修改时间
    # auto_now_add 当对象第一次被创建时自动设置当前时间
    # auto_now     每次保存对象时，自动设置该字段为当前时间。用于"最后一次修改"的时间戳
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # 这个方法用来生产url
    def get_absolute_url(self):
        return reverse('app:host_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.host_name

    class Meta:
        verbose_name = "主机信息"
        verbose_name_plural = verbose_name

class HostComment(models.Model):
    host = models.ForeignKey(Host, related_name='hostcomments')
    body = models.CharField(max_length=100, verbose_name='添加操作记录')
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default='admin')

    def __str__(self):
        return 'Comment {} {} on {}'.format(self.host, self.body, self.created)

    class Meta:
        ordering = ('-created',)
        verbose_name = "主机操作记录"
        verbose_name_plural = verbose_name