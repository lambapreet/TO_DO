from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ['id','title', 'complete', 'created']  # Fields to display in the admin panel list view
