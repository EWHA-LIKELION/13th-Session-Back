from django.contrib import admin
from .models import * #생성한 모든 모델을 가져온다는 뜻

# Register your models here.

admin.site.register(CustomUser)