# Generated by Django 5.1.1 on 2024-10-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='acounts/profile/defult/default_avatar.jpg', upload_to='acounts/profile/'),
        ),
    ]
