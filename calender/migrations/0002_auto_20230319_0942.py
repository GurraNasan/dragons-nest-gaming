# Generated by Django 3.2 on 2023-03-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
