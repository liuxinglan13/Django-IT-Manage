from .models import Host, HostGroups, Host_status, HostCategorys, HostComment
from .forms import PostForm, HostCommentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.base import View


# 基于类的首页视图  (访问控制 @login_required 登录后才可访问该视图  基于类的实现)
class IndexView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = HostComment
    context_object_name = 'host_comment_list'
    template_name = 'app/index.html'

    def get_queryset(self):
        return HostComment.objects.all()[0:5:1]


# 基于类的首页视图  (访问控制 @login_required 登录后才可访问该视图  基于类的实现)
class HostView(LoginRequiredMixin, ListView):
    # login_url = '/accounts/login/'
    # redirect_field_name = 'redirect_to'
    model = Host
    context_object_name = 'post_list'
    template_name = 'app/host.html'


# host详情视图

class HostDetailView(DetailView):
    model = Host
    template_name = 'app/host_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        response = super(HostDetailView, self).get(request, *args, **kwargs)
        comment_form = HostCommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.host = self.object
            new_comment.author = self.request.user
            new_comment.save()
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = HostCommentForm()
        comments = self.object.hostcomments.all()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context




# 基于类的 编辑更新数据视图

class HostEditView(UpdateView):
    model = Host
    form_class = PostForm
    template_name = 'app/host_edit.html'


# 基于类的创建数据视图

class HostCreateView(CreateView):
    form_class = PostForm
    template_name = 'app/host_edit.html'

# 分组筛选host的类
# url 接受两个参数 第一个 是 筛选的选项  group status category  第2个参数是 具体筛选的内容的 pk
class HostFilterView(ListView):
    model = Host
    template_name = 'app/host.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        id=self.kwargs.get('id')
        if id == 'group':
            hostgroup = get_object_or_404(HostGroups, pk=self.kwargs.get('pk'))
            return super(HostFilterView, self).get_queryset().filter(Host_group=hostgroup)
        elif id == 'status':
            host_status = get_object_or_404(Host_status, pk=self.kwargs.get('pk'))
            return super(HostFilterView, self).get_queryset().filter(host_status=host_status)
        elif id == 'category':
            host_category = get_object_or_404(HostCategorys, pk=self.kwargs.get('pk'))
            return super(HostFilterView, self).get_queryset().filter(Host_category=host_category)

