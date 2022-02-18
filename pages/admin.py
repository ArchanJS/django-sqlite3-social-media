from django.contrib import admin
from pages.models import CustomUser
from pages.models import Post
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser,UserAdmin)
admin.site.register(Post)
