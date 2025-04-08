from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import Postform
# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    form=Postform()
    return render(request, 'new.html',{'form':form})

def create(request):
    form = Postform(request.POST, request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

def delete(request, post_id):
    blog_delete=get_object_or_404(Post, pk=post_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request, post_id):
    blog_update=get_object_or_404(Post,pk=post_id)
    return render(request, 'update.html', {'blog_update':blog_update})

def update(request, post_id):
    new_blog=get_object_or_404(Post,pk=post_id)
    new_blog.title=request.POST['title']
    new_blog.body=request.POST['body']
    new_blog.save()
    return redirect('home')