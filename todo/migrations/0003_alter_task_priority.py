# Generated by Django 5.0 on 2023-12-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Migh', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50),
        ),
    ]