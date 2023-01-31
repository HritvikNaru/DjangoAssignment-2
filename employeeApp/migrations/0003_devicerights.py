# Generated by Django 4.1.5 on 2023-01-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employeeApp", "0002_devicedetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceRights",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Device_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employeeApp.devicedetails",
                    ),
                ),
                (
                    "Employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employeeApp.employeedetails",
                    ),
                ),
            ],
        ),
    ]
