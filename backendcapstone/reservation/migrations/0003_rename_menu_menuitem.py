# Generated by Django 4.2.6 on 2023-10-25 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
