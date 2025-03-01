from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import POST
# Create your views here.
def index(request):

    return render(request,'blog/index.html')

def posts(request):
    context = {
        'Posts': POST.objects.all(),
    }
    return render(request,'blog/posts.html',context)
def post(request, id):
    context = {
        'id':id,
        'Post': get_object_or_404(POST,id=id),
    }
    return render(request,'blog/Singlepost.html',context)