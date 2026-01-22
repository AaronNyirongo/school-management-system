from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ("date", "student", "present")
    list_filter = ("date", "present")
    search_fields = ("student__first_name", "student__last_name", "student__enrollment_number")
