from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

#AbstractUser django-allauth. Sin modificaciones
class User(AbstractUser):
	pass

	def __str__(self):
		return self.username


#Modelo de los Posts
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	thumbnail = models.ImageField()
	publish_date = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title

	def get_like_url(self):
		return reverse("like", kwargs={
			'slug': self.slug
		
		})

	def get_absolut_url(self):
		return reverse("detail", kwargs={
			'slug': self.slug
		
		})

	@property
	def comments(self):
		return self.comment_set.all()

	@property
	def get_comment_count(self):
		return self.comment_set.all().count()
	

	@property
	def get_view_count(self):
		return self.postview_set.all().count()


	@property
	def get_like_count(self):
		return self.like_set.all().count()

#Modelo de los Comments
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	content  = models.TextField()

	def __str__(self):
		return self.user.username


#Modelo del PostView(Vistas)
class PostView(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

#Modelo de Likes
class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
	
