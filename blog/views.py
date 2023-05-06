from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, pk= pid)
    context ={'post': post}
    return render(request, 'blog/blog-single.html',context)

def test(request):

    #posts = Post.objects.exclude(puplished_date__gt=datetime.datetime.now())
    posts = Post.objects.all()
    #time = Post.objects.dates('puplished_date','M D',order='DESC')
    context = {'posts': posts , 'time': time}
    return render(request, 'test.html',context)