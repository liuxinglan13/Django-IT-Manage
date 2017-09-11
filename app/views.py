from .models import Host
from .forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView


# 基于类的首页视图

class IndexView(ListView):
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

