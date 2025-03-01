from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class POST(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR','Draft',
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100,default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        indexes=[models.Index(fields=['publish'])]
    def __str__(self):
        return self.title