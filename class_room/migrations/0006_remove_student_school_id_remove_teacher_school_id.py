# Generated by Django 4.0.5 on 2023-11-03 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0005_remove_student_department_remove_student_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='school_id',
        ),
    ]
