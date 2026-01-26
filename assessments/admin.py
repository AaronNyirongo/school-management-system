from django.contrib import admin
from .models import Assessment, Mark

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("name", "teaching_assignment", "date", "max_score", "is_active")
    list_filter = ("is_active", "date")
    search_fields = ("name",)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("assessment", "student", "score")
    list_filter = ("assessment",)
    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__enrollment_number",
    )
