from django.http import HttpResponse
from django.shortcuts import render

from Farmer_Hand.models import BlogPost, Category


def index(request):
    posts = BlogPost.objects.all()
    if 'category' in request.GET:
        #posts = posts.filter(category=int(request.GET.get('category')))
        posts = Category.objects.get(pk = int(request.GET.get('category'))).posts.all()

    context = {
        'posts' : posts.order_by('-created_at')
    }
    return render(request,'index.html',context)

def view_post(request, pk):

    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post.html', {'post':post})

