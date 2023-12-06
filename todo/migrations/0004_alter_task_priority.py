# Generated by Django 5.0 on 2023-12-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=50),
        ),
    ]
