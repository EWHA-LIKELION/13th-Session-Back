"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import *
from accounts.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:post_id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('update_page/<int:post_id>', update_page, name='update_page'),
    path('update/<int:post_id>', update, name="update"),
    path('delete/<int:post_id>', delete, name='delete'),
    path('<int:post_id>/comment', add_comment, name="add_comment"),

    path('accounts/login', login_view, name="login"),
    path('accounts/logout', logout_view, name="logout"),
    path('accounts/signup', signup_view, name="signup")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
