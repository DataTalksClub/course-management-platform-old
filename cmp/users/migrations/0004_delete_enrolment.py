# Generated by Django 4.1.3 on 2022-11-28 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_student_enrolment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Enrolment",
        ),
    ]
