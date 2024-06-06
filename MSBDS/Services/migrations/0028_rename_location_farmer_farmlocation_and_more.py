# Generated by Django 4.2.4 on 2024-05-31 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0027_rename_user_name_farmer_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmer',
            old_name='location',
            new_name='farmLocation',
        ),
        migrations.RenameField(
            model_name='farmer',
            old_name='farm_size',
            new_name='farmSize',
        ),
        migrations.AddField(
            model_name='farmer',
            name='contact',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='farmer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]