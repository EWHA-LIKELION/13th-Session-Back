
from django.contrib import admin
from django.urls import path

import blog.views

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
]


