from django.shortcuts import render, redirect

from .models import Post


def new(request):
    return render(request, 'form.html')


def create(request):
    title = request.POST['title']
    content = request.POST['content']
    tag = request.POST['tag']

    post = Post.objects.create(
        title=title,
        content=content,
        tag=tag,
    )

    return redirect('/')


def list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'detail.html', context)














