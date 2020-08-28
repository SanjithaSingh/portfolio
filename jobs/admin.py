from django.contrib import admin
from .models import Job,Project,Stack

# Register your models here.
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Stack)