# Generated by Django 5.0 on 2024-05-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_alter_myfiles_submitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfiles',
            name='batch',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
