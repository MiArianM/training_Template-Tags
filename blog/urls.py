from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', views.post, name='postDetail'),
    path('posts/<int:id>/share', views.Ticket, name='postShare'),

]
