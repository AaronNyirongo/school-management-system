from django.contrib import admin
from .models import TeachingAssignment


@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "teacher",
        "classroom",
        "subject",
        "term",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "term", "classroom", "subject", "teacher")
    raw_id_fields = ("teacher", "classroom", "subject", "term")
    ordering = ("-created_at",)
    list_select_related = ("teacher", "classroom", "subject", "term")
