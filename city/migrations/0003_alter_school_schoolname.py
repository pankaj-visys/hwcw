# Generated by Django 5.0 on 2024-03-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_alter_book_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='schoolName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]