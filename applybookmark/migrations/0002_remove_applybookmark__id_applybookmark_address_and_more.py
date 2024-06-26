# Generated by Django 4.0.1 on 2022-02-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applybookmark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applybookmark',
            name='_id',
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='number_of_bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='number_of_bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='owner_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applybookmark',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='applybookmark',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
