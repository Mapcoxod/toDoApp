from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'owner', 'created_at', 'updated_at')
    list_filter = ('completed', 'owner', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-created_at',)