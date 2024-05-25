# Generated by Django 5.0.2 on 2024-03-27 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0015_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, choices=[('India', 'India'), ('Pakistan', 'Pakistan'), ('Ameriaca', 'America'), ('Afghanistan', 'Afghanistan'), ('London', 'London'), ('Canada', 'Canada')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=30, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.user')),
            ],
        ),
    ]