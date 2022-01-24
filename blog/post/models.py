from django.db import models
from django.contrib.auth.models import AbstractUser


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
	
