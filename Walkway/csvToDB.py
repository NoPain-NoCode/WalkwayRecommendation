import csv
import pandas as pd
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Walkway.settings')
import django
django.setup()
from maps.models import WalkwayLocation

def ctd():
    with open('./road_convert.csv','r') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)

    ss = []

    for i in range(len(s)):
        st = (s['category'][i], s['region'][i], s['distance'][i], s['time_required'][i], s['level'][i], s['course_name'][i], s['point_number'][i], s['point_name'][i], s['longitude'][i], s['latitude'][i])
        ss.append(st)

    for i in range(len(s)):
        WalkwayLocation.objects.create(category=ss[i][0], region=ss[i][1], distance=ss[i][2], time_required=ss[i][3], level=ss[i][4], course_name=ss[i][5], point_number=ss[i][6], point_name=ss[i][7], longitude=ss[i][8], latitude=ss[i][9])

if __name__ == '__main__':
    ctd()
    