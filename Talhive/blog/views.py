from django.shortcuts import render

from .models import Blog

def index(request):
    blogs = Blog.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'blog': blogs
    }

    return render(request, 'blog/blog.html', context)

def details(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'blog': blog
    }

    return render(request, 'blog/details.html', context)