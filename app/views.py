from django.shortcuts import render
from .models import Host
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse


# 首页的视图

def index(request):
    post_list = Host.objects.all()
    context = {'post_list': post_list}
    return render(request, 'app/index.html', context)


# host详情视图

class HostDetailView(DetailView):
    model = Host
    template_name = 'app/host_detail.html'
    context_object_name = 'post'


# 编辑内容的视图

def host_edit(request, pk):
    post = get_object_or_404(Host, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # post = form.save(commit=False)
            post.save()
            print("编辑成功")
    else:
        form = PostForm(instance=post)
    return render(request, 'app/host_edit.html', {'form': form})

# 新增新主机信息的视图

def host_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()
    return render(request, 'app/host_edit.html', {'form': form})