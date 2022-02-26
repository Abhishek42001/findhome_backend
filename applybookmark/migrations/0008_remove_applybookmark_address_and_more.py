# Generated by Django 4.0.2 on 2022-02-26 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applybookmark', '0007_applybookmark_user_id_alter_applybookmark_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applybookmark',
            name='address',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='city',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='description',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='number_of_bathrooms',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='number_of_bedrooms',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='price',
        ),
        migrations.RemoveField(
            model_name='applybookmark',
            name='title',
        ),
        migrations.CreateModel(
            name='Item_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=20)),
                ('user_id_foriegn_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ss', to='applybookmark.applybookmark')),
            ],
        ),
    ]
