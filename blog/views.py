from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    paginator = Paginator(POST.objects.all(), 2)
    page_num = request.GET.get('page', 1)
    try:
        Posts = paginator.page(page_num)
    except EmptyPage:
        Posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        Posts = paginator.page(1)
    context = {
        'Posts': Posts,
    }
    return render(request, 'blog/posts.html', context)


def post(request, id):
    context = {
        'id': id,
        'Post': get_object_or_404(POST, id=id),
    }
    return render(request, 'blog/Singlepost.html', context)
