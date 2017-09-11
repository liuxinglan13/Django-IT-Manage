from .models import Host, HostGroups, Host_status, HostCategorys
from .forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# 基于类的首页视图  (访问控制 @login_required 登录后才可访问该视图  基于类的实现)
class IndexView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Host
    context_object_name = 'post_list'
    template_name = 'app/index.html'


# host详情视图

class HostDetailView(DetailView):
    model = Host
    template_name = 'app/host_detail.html'
    context_object_name = 'post'


# 基于类的 编辑更新数据视图

class HostEditView(UpdateView):
    model = Host
    form_class = PostForm
    template_name = 'app/host_edit.html'


# 基于类的创建数据视图

class HostCreateView(CreateView):
    form_class = PostForm
    template_name = 'app/host_edit.html'


# 主机组  视图（点击显示相应主机组下的所有主机）
class HostGroupView(ListView):
    # 这一部分和 IndexView 差不多  所有可以 通过 继承来 减少代码 类似 class CategoryView(IndexView):
    model = Host
    template_name = 'app/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # 在类视图中，从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里，
        # 非命名组参数值保存在实例的 args 属性（是一个列表）里。所以我们使了 self.kwargs.get('pk') 来获取从 URL 捕获的分类 id 值。
        # 反正 cate 取出来的就是 ID为pk 的一个 Category 实例
        hostgroup = get_object_or_404(HostGroups, pk=self.kwargs.get('pk'))
        # 调用父类的get_queryset方法（Host_group 指的是 Host模型中需要 过滤的属性 ）
        return super(HostGroupView, self).get_queryset().filter(Host_group=hostgroup)

# 主机状态
class HostStatusView(ListView):
    # 这一部分和 IndexView 差不多  所有可以 通过 继承来 减少代码 类似 class CategoryView(IndexView):
    model = Host
    template_name = 'app/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # 在类视图中，从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里，
        # 非命名组参数值保存在实例的 args 属性（是一个列表）里。所以我们使了 self.kwargs.get('pk') 来获取从 URL 捕获的分类 id 值。
        # 反正 cate 取出来的就是 ID为pk 的一个 Category 实例
        host_status = get_object_or_404(Host_status, pk=self.kwargs.get('pk'))
        # 调用父类的get_queryset方法（Host_group 指的是 Host模型中需要 过滤的属性 ）
        return super(HostStatusView, self).get_queryset().filter(host_status=host_status)

# 主机分类
class HostCategorysView(ListView):
    # 这一部分和 IndexView 差不多  所有可以 通过 继承来 减少代码 类似 class CategoryView(IndexView):
    model = Host
    template_name = 'app/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # 在类视图中，从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里，
        # 非命名组参数值保存在实例的 args 属性（是一个列表）里。所以我们使了 self.kwargs.get('pk') 来获取从 URL 捕获的分类 id 值。
        # 反正 cate 取出来的就是 ID为pk 的一个 Category 实例
        host_category = get_object_or_404(HostCategorys, pk=self.kwargs.get('pk'))
        # 调用父类的get_queryset方法（Host_group 指的是 Host模型中需要 过滤的属性 ）
        return super(HostCategorysView, self).get_queryset().filter(Host_category=host_category)