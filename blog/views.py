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

    #Start Update Counted_views
    post.counted_views = post.counted_views +1
    post.save()
    #End Update Counted_views

    #Start looking for NextPost and PrevPost
    i = -1
    if post != None  :
        for n in posts:
            i = i+1
            if n.id == post.id:
                break
    
        if i==0:
            pre_post = posts[len(posts)-1]  
        else:
            pre_post= posts[i-1]

        if i== (len(posts)-1):
            next_post = posts[0]  
        else:
            next_post = posts[i+1]
     #End looking for NextPost and PrevPost

    context ={'post': post, 'pre_post':pre_post , 'next_post':next_post}
    return render(request, 'blog/blog-single.html',context)

def test(request):
    return render(request, 'test.html')