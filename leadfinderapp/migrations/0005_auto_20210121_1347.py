# Generated by Django 3.1.3 on 2021-01-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadfinderapp', '0004_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=2, max_length=4000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='profile_pic',
            field=models.ImageField(blank=True, default='undraw_profile_1.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='undraw_profile_1.svg', null=True, upload_to=''),
        ),
    ]