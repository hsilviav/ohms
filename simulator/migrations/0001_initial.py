# Generated by Django 4.2.2 on 2023-07-10 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ohms_app", "0002_customuser_age_customuser_specialisation_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Smartwatch",
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
                ("pulse", models.IntegerField()),
                ("systolic", models.IntegerField()),
                ("diastolic", models.IntegerField()),
                ("body_temperature", models.FloatField()),
                ("steps", models.IntegerField()),
                ("recorded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ohms_app.patient",
                    ),
                ),
            ],
        ),
    ]