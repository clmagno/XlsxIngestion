# Generated by Django 5.0.2 on 2024-02-15 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_test_tabl'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test_tabl',
        ),
        migrations.DeleteModel(
            name='test_table',
        ),
    ]
