from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
from .filters import BlogFilter
# Create your views here.

def blog_post(request):
    Blogs = Blog.objects.all().order_by('-date')
    blog_filter = BlogFilter(request.GET, queryset=Blogs)
    p = Paginator(Blogs, 2)
    page = request.GET.get('page')
    Blogs = p.get_page(page)
    return render(request, 'blog/blog_post.html',{'Blogs':Blogs, 'filter':blog_filter})

def blog_page(request, slug):
    
    mypage = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog_page.html',{'mypage':mypage})

def search_page(request):
    if request.method =='POST':
        searched = request.POST['searched']
        Blogs = Blog.objects.filter(title__icontains=searched)
    return render(request, 'blog/search_page.html',{'Blogs':Blogs,'searched':searched})

