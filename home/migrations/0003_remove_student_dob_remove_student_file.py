# Generated by Django 5.0 on 2024-01-04 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]
