# Generated by Django 3.1.7 on 2021-03-05 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walkwaylocation',
            old_name='number',
            new_name='point_number',
        ),
    ]
