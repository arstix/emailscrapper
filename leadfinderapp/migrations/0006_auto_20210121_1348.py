# Generated by Django 3.1.3 on 2021-01-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadfinderapp', '0005_auto_20210121_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]