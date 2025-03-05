from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class POST(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft',
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    reading_time = models.IntegerField(default=0)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['publish'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:postDetail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(POST, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return self.title
