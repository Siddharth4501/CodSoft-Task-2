# Generated by Django 4.2.4 on 2023-08-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('ph_no', models.IntegerField(max_length=12)),
                ('message', models.CharField(max_length=120)),
            ],
        ),
    ]