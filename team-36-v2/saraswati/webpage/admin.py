from django.contrib import admin
from .models import teacher_db, student_db

# Register your models here.
admin.site.register(teacher_db)
admin.site.register(student_db)
 