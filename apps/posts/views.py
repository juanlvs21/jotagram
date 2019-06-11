"""Posts views."""
# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile
from apps.posts.models import Post

# Form
from apps.posts.forms import PostForm

@login_required
def list_post(request):
    """List existing posts."""
    profile = request.user.profile
    posts = Post.objects.all().order_by('-created')
    return render(
        request=request,
        template_name='posts/posts.html',
        context={
            'profile':profile,
            'user': request.user,
            'posts':posts
        }
    )

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('so sad')
    
    else:
        form = PostForm()
    
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )