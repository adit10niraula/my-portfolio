# Generated by Django 5.0.1 on 2024-05-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
