# Generated by Django 2.1.6 on 2019-03-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superIndex', '0007_auto_20190306_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5),
        ),
    ]