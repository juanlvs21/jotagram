"""okamigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf import settings

# from okamigram import views as local_views
from apps.posts import views as post_views
from apps.users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', local_views.hello),
    # path('sorted/', local_views.sorted_integers),
    # path('hi/<str:name>/<int:age>', local_views.say_hi),

    path('', post_views.list_post, name="home"),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
