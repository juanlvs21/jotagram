"""Posts URLs."""
# Django
from django.urls import path

# Views
from apps.users import views

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('me/profile/picture', views.UpdatePictureView.as_view(), name='update_picture'),
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
]