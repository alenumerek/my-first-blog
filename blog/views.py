from django.shortcuts import render
from django.utils import timezone
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', { 'blogs': blogs }) #zawżyj template -> blog -> plik html