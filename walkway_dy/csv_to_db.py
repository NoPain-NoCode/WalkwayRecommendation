import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "walkway_dy.settings")
django.setup()

from maps.models import WalkwayLocation

CSV_PATH = './road_convert.csv'


queryset = WalkwayLocation.objects.all()
queryset.delete()

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        WalkwayLocation.objects.create(
            category=row['category'],
            region=row['region'],
            distance=row['distance'],
            time_required=row['time_required'],
            level=row['level'],
            course_name=row['course_name'],
            point_number=row['point_number'],
            point_name=row['point_name'],
            longitude=row['long_'],
            latitude=row['lat_'],
        )