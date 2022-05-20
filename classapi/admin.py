from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','email','boolean','date','city','desc']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','email','boolean','date','subject']    