from django.contrib import admin
from .models import Post, Comment, Hashtag # * 하나로 처리해도 괜찮다.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hashtag)
