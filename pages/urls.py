from django.urls import path
from .views import (CreatePostView, 
    DeletePostView, HomePageView,
    IndPostView, 
    UpdatePostView)
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('post/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('post/<int:pk>',
    IndPostView.as_view(),name='post_detail'),
    path('post/new',CreatePostView.as_view(),
    name='new_post'),
    path('post/<int:pk>/edit',
    UpdatePostView.as_view(),name='post_edit')
]