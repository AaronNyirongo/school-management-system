from django.contrib import admin
from .models import Assessment, Mark


class MarkInline(admin.TabularInline):
    model = Mark
    extra = 0
    raw_id_fields = ("student",)
    fields = ("student", "score", "comment", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "teaching_assignment",
        "term",
        "date",
        "max_score",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "term", "date")
    raw_id_fields = ("teaching_assignment", "term")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    inlines = [MarkInline]


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("id", "assessment", "student", "score", "percent", "created_at")
    list_filter = ("assessment",)
    raw_id_fields = ("assessment", "student")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    def percent(self, obj):
        try:
            max_score = obj.assessment.max_score if obj.assessment else None
            if max_score:
                return round((float(obj.score) / float(max_score)) * 100, 2)
        except Exception:
            return ""
        return ""

    percent.short_description = "Percent (%)"
