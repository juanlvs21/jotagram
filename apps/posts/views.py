"""Posts views."""
# Django
# from django.shortcuts import render
from django.shortcuts import render

# Utilities
from datetime import datetime

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

def list_post(request):
    """List existing posts."""
    return render(request, 'posts.html', {'posts':posts})
