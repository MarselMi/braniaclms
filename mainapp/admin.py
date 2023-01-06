from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preamble", "body"]


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "num", "title", "deleted"]
    ordering = ["-course", "-num"]
    list_per_page = 5
    list_filter = ["course", "created_ad", "deleted"]
    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Отметить удаленным")

admin.site.register(mainapp_models.Course)


@admin.register(mainapp_models.CourseTeacher)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "get_courses"]
    list_select_related = True
    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.course.all()))
    get_courses.short_description = _("Курсы")