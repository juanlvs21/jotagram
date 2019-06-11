"""Users views."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile

# Forms
from apps.users.forms import ProfileForm, PictureForm

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')

def signup_view(request):
    """Sign up a user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError as err:
            print(err)
            return render(request, 'users/signup.html', {'error': 'Username or Email is already in user'})
    
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        profile = Profile(user=user,picture='users/pictures/perfil.png')
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        formProfile = ProfileForm(request.POST)

        if formProfile.is_valid():
            dataProfile = formProfile.cleaned_data
            profile.website = dataProfile['website']
            profile.biography = dataProfile['biography']
            profile.phone_number = dataProfile['phone_number']
            profile.save()
            return redirect('update_profile')
                
    else:
        formProfile = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'formProfile': formProfile,
        }
    )

@login_required
def update_picture(request):
    """Update a user's picture view."""
    profile = request.user.profile

    if request.method == 'POST':
        formPicture = PictureForm(request.POST, request.FILES)

        if formPicture.is_valid():
            dataPicture = formPicture.cleaned_data
            profile.picture = dataPicture['picture']
            profile.save()
            return redirect('update_profile')                
    else:
        formPicture = PictureForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'formPicture': formPicture
        }
    )

