from django.contrib import admin
from .models import TeachingAssignment

@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "subject", "classroom", "is_active")
    list_filter = ("is_active", "classroom", "subject")
    search_fields = (
        "teacher__first_name",
        "teacher__last_name",
        "teacher__employee_number",
        "subject__name",
        "subject__code",
    )
