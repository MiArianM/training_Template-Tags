from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = POST
    paginate_by = 1
    context_object_name = 'Posts'
    template_name = 'blog/posts.html'


def post(request, id):
    context = {
        'id': id,
        'Post': get_object_or_404(POST, id=id),
    }
    return render(request, 'blog/Singlepost.html', context)
