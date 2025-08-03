from django.contrib import admin
from apitest.models import LessionList

# Register your models here.
@admin.register(LessionList)
class LessionListAdmin(admin.ModelAdmin):
    list_display = ['title','lession','lession_details']