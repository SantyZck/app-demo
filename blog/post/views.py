from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Comment, Like
from .forms import PostForm
from django.urls import reverse_lazy

class PostListView(ListView):
	model = Post


class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	
	form_class = PostForm

	success_url = '/'	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'view_type': 'create'
			})
		return context

class PostUpdateView(UpdateView):
	model = Post

	fields = (
		'title', 
		'content', 
		'thumbnail', 
		'author', 
		'slug'
	)
	success_url = '/'	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'view_type': 'update'
			})
		return context

class PostDeleteView(DeleteView):
	model = Post

	success_url = '/'