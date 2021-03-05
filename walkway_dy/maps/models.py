from django.db import models

# Create your models here.
class WalkwayLocation(models.Model):
   category = models.CharField(max_length=255)
   region = models.CharField(max_length=255)
   distance = models.CharField(max_length=255)
   time_required = models.CharField(max_length=255)
   level = models.IntegerField()
   course_name = models.CharField(max_length=255)
   point_number = models.IntegerField()
   point_name = models.CharField(max_length=255)
   longitude = models.FloatField()
   latitude  = models.FloatField()
   
   class Meta:
       db_table = 'WalkwayLocation'