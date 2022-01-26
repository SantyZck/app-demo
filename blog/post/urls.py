from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	like
)


urlpatterns = [
	path('', PostListView.as_view(), name='list'),
	path('create/', PostCreateView.as_view(), name='create'),
	path('<slug>/', PostDetailView.as_view(), name='detail'),
	path('<slug>/update', PostUpdateView.as_view(), name='update'),
	path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
	path('like/<slug>/', like, name='like')
]