# Generated by Django 4.1.5 on 2023-01-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeDetails",
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
                ("FirstName", models.CharField(max_length=100)),
                ("LastName", models.CharField(max_length=100)),
                ("MobileNumber", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=254)),
                ("Address", models.CharField(max_length=200)),
            ],
        ),
    ]