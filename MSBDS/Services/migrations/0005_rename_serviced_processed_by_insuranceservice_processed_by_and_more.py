# Generated by Django 4.2.5 on 2023-09-18 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_alter_insuranceservice_serviced_processed_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insuranceservice',
            old_name='serviced_processed_by',
            new_name='processed_by',
        ),
        migrations.RenameField(
            model_name='licenseservice',
            old_name='serviced_processed_by',
            new_name='processed_by',
        ),
    ]
