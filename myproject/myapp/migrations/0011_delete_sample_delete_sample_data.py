# Generated by Django 5.0.2 on 2024-02-15 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_sample_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sample',
        ),
        migrations.DeleteModel(
            name='sample_data',
        ),
    ]
