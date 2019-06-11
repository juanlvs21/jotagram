"""Posts views."""
# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile

# Form
from apps.posts.forms import PostForm

posts = [
    {
        'title':'Mont Blac',
        'user':{
            'name':'Yésica Cortés',
            'picture':'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/500/500/?image=1036',
    },
    {
        'title':'Via Láctea',
        'user':{
            'name':'Christian Van der Henst',
            'picture':'https://picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/500/500/?image=903',
    },
    {
        'title':'Nuevo auditorio',
        'user':{
            'name':'Uriel (Thespianartist)',
            'picture':'https://picsum.photos/60/60/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/500/500/?image=1076',
    },
]

@login_required
def list_post(request):
    """List existing posts."""
    # return render(request, 'posts/posts.html', {'posts':posts})
    profile = request.user.profile
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