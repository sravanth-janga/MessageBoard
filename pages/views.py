from django.db import models
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'home.html'

class IndPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

class CreatePostView(CreateView):
    model = Post
    fields = ['title','author','body']
    template_name = 'post_new.html'
class UpdatePostView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'post_edit.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')