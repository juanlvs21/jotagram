"""Users views."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms
from apps.users.forms import ProfileForm, PictureForm, SignupForm

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
       form = SignupForm(request.POST)

       if form.is_valid():
           form.save()
           return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name= 'users/signup.html',
        context={
            'form':form
        }
    )

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

