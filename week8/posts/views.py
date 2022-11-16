from django.shortcuts import render, redirect
from posts.models import Post
from django.urls import reverse


# Create Form HTML 응답
def new(reqeust):
    return render(reqeust, 'form.html')
    # posts/templates


# Create 데이터 생성
def create(request):
    # 1. 클라이언트 데이터 확인
    title = request.POST['title']
    content = request.POST['content']
    tag = request.POST['tag']
    print(title)
    print(content)
    print(tag)
    # 2. 모델 데이터 생성
    Post.objects.create(
        title=title,
        content=content,
        tag=tag,
    )
    # 3. 응답
    # return redirect('/new/')
    # return redirect('https://www.naver.com')
    return redirect('/')


# 기능 구현 순서 M -> V -> URL -> T
def list(request):
    # 1. 데이터 조회
    post_list = Post.objects.all()
    data = {
        'post_list': post_list
    }
    # 2. 응답
    return render(request, 'list.html', data)


def detail(request, id):
    # 1. 데이터 조회
    post = Post.objects.get(id=id)
    data = {
        'post': post,
    }
    # 2. 응답
    return render(request, 'detail.html', data)


from django.urls import reverse
def edit(request, id):
    post = Post.objects.get(id=id)
    data = {'post': post}
    return render(request, 'form.html', data)


def update(request, id):
    post = Post.objects.get(id=id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.tag = request.POST['tag']
    post.save()
    return redirect(reverse('detail', kwargs={'id': id}))

def confirm_delete(request, id):
    post = Post.objects.get(id=id)
    data = {'post': post}
    return render(request, 'confirm_delete.html', data)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(reverse('list'))












