# Generated by Django 5.0.2 on 2024-03-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemnaFC', '0012_alter_fanpicture_fan_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanpicture',
            name='fan_picture',
            field=models.ImageField(upload_to='images'),
        ),
    ]
