
from django.contrib import admin
from django.urls import path

import blog.views
import accounts.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('post/<int:post_id>', blog.views.detail, name="detail"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('delete/<int:post_id>', blog.views.delete, name='delete'),
    path('update_page/<int:post_id>', blog.views.update_page, name='update_page'),
    path('<int:post_id>/comment', blog.views.add_comment, name='add_comment'),
    path('update/<int:post_id>', blog.views.update, name='update2'),

    path('accounts/login', accounts.views.login_view, name="login"),
    path('accounts/logout',accounts.views.logout_view,name="logout"),
    path('accounts/signup',accounts.views.signup_view,name="signup")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




