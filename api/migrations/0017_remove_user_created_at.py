# Generated by Django 5.1.3 on 2024-11-24 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_user_username_alter_user_email_alter_user_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]
