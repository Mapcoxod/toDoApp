from django.contrib import admin

from tasks.models import Task, Participant


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "completed", "owner", "created_at", "updated_at")
    list_filter = ("completed", "owner", "created_at")
    search_fields = ("title", "description", "owner__username")
    ordering = ("-created_at",)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "bin",
        "status",
        "created_at",
        "issue_date",
        "expiration_date",
        "updated_at",
    )
    list_filter = ("status", "created_at", "issue_date", "expiration_date")
    search_fields = ("company_name", "bin")
    ordering = ("-created_at",)
