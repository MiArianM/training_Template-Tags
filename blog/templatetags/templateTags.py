from django import template
from ..models import POST
from django.db.models import Min
from django.db.models import Max

register = template.Library()


# For Knowing count of posts
@register.simple_tag
def posts_count():
    return POST.objects.count()


# For getting the Most and lowest Reading time values
@register.simple_tag
def RT_Most():
    Most_rt = POST.objects.aggregate(max_time=Max('reading_time'))['max_time']
    Most_rt_post = POST.objects.filter(reading_time=Most_rt).first()

    return f'{Most_rt_post.title} with {Most_rt_post.reading_time} posts' if Most_rt_post else "No Posts"


@register.simple_tag()
def RT_Lowest():
    Lowest_rt = POST.objects.aggregate(min_time=Min('reading_time'))['min_time']
    Lowest_rt_post = POST.objects.filter(reading_time=Lowest_rt).first()

    return f'{Lowest_rt_post.title} with {Lowest_rt_post.reading_time} posts' if Lowest_rt_post else "No Posts"


@register.filter(name='Censor')
def Censor(value):
    if type(value) == int:
        raise template.TemplateSyntaxError('Please use String values')
    else:
        if 'fuck' in value.lower():
            value = value.replace('fuck', '****')

    return value
