from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('create_post', views.CreatePost, name='creation_post'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', views.postDetail, name='postDetail'),
    path('posts/<int:id>/share', views.postShare, name='postShare'),

]
