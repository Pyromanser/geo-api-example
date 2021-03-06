# Generated by Django 3.1.1 on 2020-09-24 13:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('address', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
