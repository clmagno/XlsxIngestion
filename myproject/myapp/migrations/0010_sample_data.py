# Generated by Django 5.0.2 on 2024-02-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_test_table_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Office Type', models.CharField(max_length=255)),
                ('Regional Office/ Division Office', models.CharField(max_length=255)),
                ('Asset Classification', models.CharField(max_length=255)),
                ('Asset Sub Class', models.CharField(max_length=255)),
                ('UACS Object Code', models.CharField(max_length=255)),
                ('Asset Item/ Article', models.CharField(max_length=255)),
                ('Manufacturer', models.CharField(max_length=255)),
                ('Model', models.CharField(max_length=255)),
                ('Serial Number', models.CharField(max_length=255)),
                ('Specification/Description', models.CharField(max_length=255)),
                ('Property Number', models.CharField(max_length=255)),
                ('Current Condition', models.CharField(max_length=255)),
                ('Source of Fund', models.CharField(max_length=255)),
                ('Cost of Acquisition', models.CharField(max_length=255)),
            ],
        ),
    ]
