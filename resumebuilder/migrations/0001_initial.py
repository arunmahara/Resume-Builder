# Generated by Django 4.2 on 2023-04-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("social", models.URLField(blank=True)),
                ("number", models.PositiveBigIntegerField()),
                ("objective", models.TextField()),
                ("company_name", models.CharField(max_length=100)),
                ("job_title", models.CharField(max_length=50)),
                ("job_works", models.TextField()),
                ("job_date_from", models.DateField()),
                ("job_date_to", models.DateField()),
                ("college_name", models.CharField(max_length=100)),
                ("course", models.CharField(max_length=50)),
                ("course_modules", models.TextField()),
                ("gpa", models.DecimalField(decimal_places=1, max_digits=2)),
                ("skills", models.CharField(max_length=150)),
                ("profile_picture", models.ImageField(upload_to="pics")),
            ],
        ),
    ]
