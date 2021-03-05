from django.contrib import admin
from .models import WalkwayLocation
# Register your models here.
class WalkwayAdmin(admin.ModelAdmin):
    list_display = ('point_name', 'point_number')

admin.site.register(WalkwayLocation, WalkwayAdmin)