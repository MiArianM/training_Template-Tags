from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from .forms import Ticketform
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


def Ticket(request, id):
    post = get_object_or_404(POST, id=id)
    sent = False
    if (request.method == "POST"):
        form = Ticketform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        post_url = request.build_absolute_uri(post.get_absolute_url())
        subject = f"{cd['name']} Recommends you read " f"{post.title}"
        message = f"Read {post.title} at {post_url}\n\n" \
                  f"{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, cd['email'], [cd['to']])
        sent = True
    else:
        form = Ticketform()
    context = {
        'form': form,
        'post': post,
        'sent': sent,
    }
    return render(request, 'forms/share.html', context)
