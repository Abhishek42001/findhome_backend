# Generated by Django 4.0.2 on 2022-02-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applybookmark', '0009_alter_applybookmark_user_id_alter_item_id_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_id',
            name='item_id',
            field=models.IntegerField(unique=True),
        ),
    ]
