"""Posts URLs."""
# Django
from django.urls import path

# Views
from apps.posts import views

urlpatterns = [
    path('', views.PostsFeedViews.as_view(), name="home"),
    path('posts/new', views.CreatePostView.as_view(), name="create_post"),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name="detail_post"),
]