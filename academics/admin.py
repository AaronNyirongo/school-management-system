from django.contrib import admin
from .models import ClassRoom

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("level", "stream", "year")
    list_filter = ("level", "year")
    search_fields = ("stream",)
    filter_horizontal = ("subjects",)
