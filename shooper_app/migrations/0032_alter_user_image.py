# Generated by Django 5.0 on 2024-04-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0031_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='https://bootdey.com/img/Content/avatar/avatar7.png', upload_to='media'),
        ),
    ]