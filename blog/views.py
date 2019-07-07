from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def posts_list(request):
    all_posts = Post.objects.all()
    logged_user = Author.objects.filter(user=request.user).first()
    context = {
        'all_posts': all_posts,
        'all_posts2': all_posts.filter(author=logged_user),
    }
    return render(request, 'posts/posts_lists.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        phone=8989898989
    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'posts/posts_create.html', context)


def post_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None,
                         instance=unique_post)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }

    return render(request, 'posts/post_update.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

