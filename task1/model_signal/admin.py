from django.contrib import admin
from model_signal.models import (
    CourseLog,
    CourseModel
)

# Register your models here.
@admin.register(CourseModel)
class CourseModel(admin.ModelAdmin):
    list_display = ['course_name','course_number']

@admin.register(CourseLog)
class CourseLogModel(admin.ModelAdmin):
    list_display = ['course','details']
