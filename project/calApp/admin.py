from django.contrib import admin
# importing the teacher model into the admin
from .models import User


# admin.site.register(Teacher)
admin.site.register(User)
# Register your models here.
