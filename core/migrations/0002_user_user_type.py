# Generated by Django 4.0.5 on 2023-01-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
