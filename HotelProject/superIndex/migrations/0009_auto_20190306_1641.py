# Generated by Django 2.1.6 on 2019-03-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superIndex', '0008_auto_20190306_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], max_length=9),
        ),
    ]
