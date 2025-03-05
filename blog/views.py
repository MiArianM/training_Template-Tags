from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = POST
    paginate_by = 4
    context_object_name = 'post_list'
    template_name = 'blog/posts.html'


def postDetail(request, id):
    context = {
        'id': id,
        'Post': get_object_or_404(POST, id=id),
    }
    return render(request, 'blog/Singlepost.html', context)


def postShare(request, id):
    ticket_obj = POST.objects.create()
    if (request.method == "POST"):
        form = Ticketform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ticket_obj.subject = cd['subject']
            ticket_obj.message = cd['message']
            ticket_obj.save()
            redirect('blog:DetailPost', id=id)
    else:
        form = Ticketform()
    context = {
        'form': form,
    }
    return render(request, 'forms/share.html', context)


def CreatePost(request):
    if (request.method == "POST"):
        form = Postform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_obj = form.save(commit=False)
            post_obj.title = cd['title']
            post_obj.content = cd['content']
            post_obj.slug = cd['slug']
            post_obj.reading_time = cd['reading_time']
            post_obj.author = request.user
            post_obj.save()
            return redirect('blog:posts')
    else:
        form = Postform()
    context = {
        'form': form,
    }

    return render(request, 'forms/create_post.html', context)
