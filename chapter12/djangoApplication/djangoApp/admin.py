from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import post

admin.site.register(post)