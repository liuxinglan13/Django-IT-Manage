from django.contrib import admin
from .models import HostGroups, HostCategorys, Host
# Register your models here.

admin.site.register(Host)
admin.site.register(HostGroups)
admin.site.register(HostCategorys)