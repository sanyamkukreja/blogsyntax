from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.
def bloghome(request):
    allposts=Post.objects.all()
    print(f"output--{allposts}")
    context={'allposts':allposts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    print(post)
    context={'post':post}
    return render(request,'blog/blogpost.html',context)    