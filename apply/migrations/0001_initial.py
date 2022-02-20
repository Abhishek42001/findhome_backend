# Generated by Django 4.0.1 on 2022-02-20 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('typee', models.CharField(max_length=50)),
                ('main_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ApplywithImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tt', to='apply.apply')),
            ],
        ),
    ]
