from django.contrib import admin
from .models import ClassRoom, AcademicYear, Term

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("level", "stream", "year")
    list_filter = ("level", "year")
    search_fields = ("stream",)
    filter_horizontal = ("subjects",)

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "start_date", "end_date")
    list_filter = ("year",)
    search_fields = ("name", "year__name")
