# Generated by Django 4.0.2 on 2022-03-02 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_message_receiver_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='se', to='chat.sender'),
        ),
    ]
