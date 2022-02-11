from django.shortcuts import render
from .models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post(request, pk):
    posts=Posts.objects.get(id=pk)
    return render(request,'posts/posts.html',{'post':posts})
