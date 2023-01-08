from django.shortcuts import render
from home.models import Blog
# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request,'home/home.html',{
        'blog':blog
    })

def blogpage(request):
    blog = Blog.objects.all()
    return render(request,'home/blog_page.html',{
        'blog':blog
    })

def blogdetails(request,pk):
    blog = Blog.objects.get(pk=pk)
    return render(request,'home/blog_detail.html',{
        'blog':blog
    })