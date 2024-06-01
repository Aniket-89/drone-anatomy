from django.shortcuts import render

from .models import Blog

# Create your views here.


def blog_list_view(request):
    context = {
        "blogs": Blog.objects.all(),
    }
    return render(request, "blogs/blog-list.html", context)


def blog_detail_view(request, pk):
    context = {
        "blog": Blog.objects.get(pk=pk),
    }
    return render(request, "blogs/blog-detail.html", context)
