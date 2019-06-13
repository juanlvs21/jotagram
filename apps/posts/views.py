"""Posts views."""
# Django
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


# Utilities
from datetime import datetime

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile
from apps.posts.models import Post

# Form
from apps.posts.forms import PostForm

class PostsFeedViews(LoginRequiredMixin, ListView):
    template_name='posts/posts.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 5
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name='posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:home')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
