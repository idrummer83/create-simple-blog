from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def posts_list(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'posts/posts_lists.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)