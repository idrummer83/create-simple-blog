from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostModelForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)


@login_required
def posts_list(request):
    all_posts = Post.objects.all()
    logged_user = Author.objects.filter(user=request.user).first()
    users = User.objects.all()
    context = {
        'all_posts': all_posts,
        'all_posts2': all_posts.filter(author=logged_user),
        'users': users
    }
    return render(request, 'posts/posts_lists.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
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



class UserReactionView(View):
    template_name = 'posts/post_detail.html'

    def get(self, request, *args, **kwargs):
        post_id = self.request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
        like = self.request.GET.get('like')
        dislike = self.request.GET.get('dislike')

        if like and (request.user not in post.users_reaction.all()):
            post.like += 1
            post.users_reaction.add(request.user)
            post.save()
        if dislike and (request.user not in post.users_reaction.all()):
            post.dislike += 1
            post.users_reaction.add(request.user)
            post.save()
        data = {
            'like': post.like,
            'dislike': post.dislike
        }

        return JsonResponse(data)