from django import forms
from .models import Host, HostComment
from django.forms import TextInput, Select


class PostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('ip', 'host_name', 'host_purpose', 'Host_category', 'Host_group',
                  'admin_Account', 'admin_password', 'Host_operatingsystem', 'Host_body', 'host_status')

        # 重写（覆盖）默认的字段 http://python.usyiyi.cn/translate/django_182/topics/forms/modelforms.html
        # 给title 添加了一个 css class类名
        widgets = {
            'host_name': TextInput(attrs={'class': 'form-control'}),
            'host_purpose': TextInput(attrs={'class': 'form-control'}),
            'Host_category': Select(attrs={'class': 'form-control'}),
            'Host_operatingsystem': Select(attrs={'class': 'form-control'}),
        }


class HostCommentForm(forms.ModelForm):
    class Meta:
        model = HostComment
        fields = ('body',)

        widgets = {
            'body': TextInput(attrs={'class': 'form-test'}),
        }
