from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'created_at')
    search_fields = ('name', 'email', 'course')
    list_filter = ('course', 'created_at')