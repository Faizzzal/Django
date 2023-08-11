from django.contrib import admin
from app_main.models import Students, Classroom, Teachers, Marks
# Register your models here.
admin.site.register(Students)
admin.site.register(Classroom)
admin.site.register(Teachers)
admin.site.register(Marks)