from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustumUserAdmin(admin.ModelAdmin):
    pass