from django.contrib import admin
from .models import HostGroups, HostCategorys, Host, OperatingSystems, Host_status , HostComment
# Register your models here.


class HostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'host_name', 'host_purpose', 'host_status',
                    'Host_category', 'Host_group')
    list_filter = ('host_status', 'Host_category', 'Host_group')   # 过滤器
    search_fields = ('ip', 'Host_group')
    ordering = ['host_status', 'Host_category']                     # 排序

admin.site.register(Host, HostAdmin)
admin.site.register(HostGroups)
admin.site.register(HostCategorys)
admin.site.register(OperatingSystems)
admin.site.register(Host_status)
admin.site.register(HostComment)
