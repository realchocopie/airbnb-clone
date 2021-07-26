from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Roomtype, models.Amenity, models.Facility, models.HouseRule)
class RoomTypeAdmin(admin.ModelAdmin):
    pass
