# Generated by Django 4.0.2 on 2022-03-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('timestamp',)},
        ),
    ]
