from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/upvote/', views.upvote_post, name='upvote_post'),
    path('create/', views.create_post, name='create_post'),
    path('register/', views.register, name='register')
]