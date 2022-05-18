from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Singer)
class AdminSinger(admin.ModelAdmin):
    list_display = ['title','name','apdate','city']
    list_per_page = 10
    search_fields = ['title','name']
    list_filter = ['title','name']



@admin.register(Song)
class AdminSinger(admin.ModelAdmin):
    list_display = ['title','son_name','writer','singer']
    list_per_page = 10
    search_fields = ['title','son_name','writer', 'singer']
    list_filter = ['son_name','writer', 'singer']

