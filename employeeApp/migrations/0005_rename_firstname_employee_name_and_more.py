# Generated by Django 4.1.5 on 2023-02-08 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employeeApp", "0004_device_historicaldevice_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee", old_name="FirstName", new_name="Name",
        ),
        migrations.RenameField(
            model_name="historicalemployee", old_name="FirstName", new_name="Name",
        ),
        migrations.RemoveField(model_name="employee", name="LastName",),
        migrations.RemoveField(model_name="historicalemployee", name="LastName",),
    ]
