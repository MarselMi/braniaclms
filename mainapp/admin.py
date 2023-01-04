from django.contrib import admin
from . import models


admin.site.register(models.News)
admin.site.register(models.Course)
admin.site.register(models.CourseTeacher)
admin.site.register(models.Lesson)