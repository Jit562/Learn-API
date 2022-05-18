from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Singer)
class AdminSinger(admin.ModelAdmin):
    list_display = ['name','gender']
    list_per_page = 10
    search_fields = ['name']
    list_filter = ['name']



@admin.register(Song)
class AdminSinger(admin.ModelAdmin):
    list_display = ['title','singer','duration']
    list_per_page = 10
    search_fields = ['title']
    

