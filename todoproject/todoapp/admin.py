from django.contrib import admin
from .models import TodoListItem

class TodoAdmin(admin.ModelAdmin):
    list_display = ('content', 'date', 'time')

admin.site.register(TodoListItem, TodoAdmin)