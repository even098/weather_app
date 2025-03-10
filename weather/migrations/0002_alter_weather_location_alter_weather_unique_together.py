# Generated by Django 5.1.6 on 2025-02-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together={('location', 'country')},
        ),
    ]
