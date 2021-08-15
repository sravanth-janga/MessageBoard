from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class HomePageView(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'home.html'