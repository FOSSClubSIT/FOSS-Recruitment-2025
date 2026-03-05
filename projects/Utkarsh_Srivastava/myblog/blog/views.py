from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")

        if author and text:
            Comment.objects.create(post=post, author=author, text=text)

        return redirect('post_detail', pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.upvotes += 1
    post.save()
    return redirect('post_detail', pk=pk)


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(
                author=request.user,
                title=title,
                content=content
            )
            return redirect('home')

    return render(request, 'blog/create_post.html')


@login_required
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user not in post.upvotes.all():
        post.upvotes.add(request.user)

    return redirect('post_detail', pk=pk)



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('login')

    return render(request, 'blog/register.html')