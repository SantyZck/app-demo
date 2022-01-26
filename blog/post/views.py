from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Comment, Like
from .forms import PostForm
from .forms import CommentForm
from django.urls import reverse_lazy

class PostListView(ListView):
	model = Post


class PostDetailView(DetailView):
	model = Post

	def post(self, *args, **kwargs):
		form = CommentForm(self.request.POST)
		if form.is_valid():
			post = self.get_object()
			#Instance form
			comment = form.instance
			#User comment
			comment.user = self.request.user
			comment.post = post
			comment.save()
			return redirect("detail", slug=post.slug)
		return redirect('detail', slug=self.get_object().slug)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'form': CommentForm()
			})
		return context



	def get_object(self, **kwargs):
		object = super().get_object(**kwargs)
		if self.request.user.is_authenticated:
			PostView.objects.get_or_create(user=self.request.user, post=object)

		return object


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
	form_class = PostForm

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

def like(request, slug):
	post = get_object_or_404(Post, slug=slug)
	like_qs = Like.objects.filter(user=request.user, post=post)

	if like_qs.exists():
		like_qs[0].delete()
		return redirect('detail', slug=slug)
	Like.objects.create(user=request.user, post=post)
	return redirect('detail', slug=slug)
