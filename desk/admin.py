from django.contrib import admin
 
# Register your models here.
from desk.models import Task, TaskList, Category, Status, Priority
 
class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task
 
admin.site.register(Task,TaskAdmin)
admin.site.register(TaskList)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Priority)

