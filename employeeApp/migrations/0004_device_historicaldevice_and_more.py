# Generated by Django 4.1.5 on 2023-02-07 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("employeeApp", "0003_alter_devicedetails_employeeassigned_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("Name", models.CharField(max_length=100)),
                ("Type", models.CharField(max_length=100)),
                ("Cost", models.IntegerField()),
                ("Allocated", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalDevice",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Type", models.CharField(max_length=100)),
                ("Cost", models.IntegerField()),
                ("Allocated", models.BooleanField(default=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical device",
                "verbose_name_plural": "historical devices",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RenameModel(
            old_name="HistoricalEmployeeDetails", new_name="HistoricalEmployee",
        ),
        migrations.RemoveField(
            model_name="historicaldevicedetails", name="EmployeeAssigned",
        ),
        migrations.RemoveField(
            model_name="historicaldevicedetails", name="history_user",
        ),
        migrations.AlterModelOptions(
            name="historicalemployee",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical employee",
                "verbose_name_plural": "historical employees",
            },
        ),
        migrations.RenameModel(old_name="EmployeeDetails", new_name="Employee",),
        migrations.DeleteModel(name="DeviceDetails",),
        migrations.DeleteModel(name="HistoricalDeviceDetails",),
        migrations.AddField(
            model_name="historicaldevice",
            name="EmployeeAssigned",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="employeeApp.employee",
            ),
        ),
        migrations.AddField(
            model_name="historicaldevice",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="EmployeeAssigned",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee",
                to="employeeApp.employee",
            ),
        ),
    ]
