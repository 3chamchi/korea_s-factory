from django.shortcuts import render, redirect
from django.urls import reverse

from posts.models import Post

# 기능 구현 순서 M -> V -> URL -> T
# 부트스트랩 템플릿 index2.html 적용
def index(request):
    post_list = Post.objects.all()
    data = {
        'post_list': post_list
    }
    return render(request, 'index2.html', data)

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


# 기능 구현 순서 M -> V -> URL -> T

# 업데이트 1. 수정을 위한 HTML 응답
def edit(request, id):
    # 1. 데이터 조회
    post = Post.objects.get(id=id)  # 데이터베이스에서 데이터 조회
    data = {'post': post}
    # 2. HTML 응답
    return render(request, 'form.html', data)  # HTML 응답


# 업데이트 2. 데이터 수정
def update(request, id):
    # 1. 데이터 조회
    post = Post.objects.get(id=id)  # 데이터베이스에서 데이터 조회
    # 2. 데이터 저장
    post.title = request.POST['title']  # 클라이언트가 보낸 title 덮어쓰기
    post.content = request.POST['content']  # 클라이언트가 보낸 content 덮어쓰기
    post.tag = request.POST['tag']  # 클라이언트가 보낸 tag 덮어쓰기
    post.save()  # 데이터베이스에 데이터 갱신 처리 / 실제 데이터베이스 데이터 수정
    # 3. 리다이렉트 응답
    return redirect(reverse('detail', kwargs={'id': post.id}))

# 기능 구현 순서 M -> V -> URL -> T
# 삭제 1. 삭제 여부 확인
def confirm_delete(request, id):
    # 1. 데이터 조회
    post = Post.objects.get(id=id)  # 데이터베이스에서 데이터 조회
    # 2. HTML 응답
    return render(request, 'confirm_delete.html', {'post': post})

# 삭제 2. 데이터 삭제
def delete(request, id):
    # 1. 데이터 조회
    post = Post.objects.get(id=id)  # 데이터베이스 데이터 조회
    # 2. 데이터 삭제
    post.delete()  # 데이터베이스 데이터 삭제
    # 3. 응답 / 리다이렉트
    return redirect(reverse('list'))
