from django.contrib import admin
from .models import HostGroups, HostCategorys, Host, OperatingSystems
# Register your models here.

admin.site.register(Host)
admin.site.register(HostGroups)
admin.site.register(HostCategorys)
admin.site.register(OperatingSystems)