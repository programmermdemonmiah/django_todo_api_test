# Generated by Django 5.1.3 on 2024-11-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile_image.png', upload_to='users/images/'),
        ),
    ]
