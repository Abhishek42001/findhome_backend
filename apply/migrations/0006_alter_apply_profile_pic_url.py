# Generated by Django 4.0.2 on 2022-03-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_apply_profile_pic_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='profile_pic_url',
            field=models.CharField(max_length=1000),
        ),
    ]