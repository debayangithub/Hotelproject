# Generated by Django 2.1.6 on 2019-03-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superIndex', '0005_customer_cust_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_id',
            field=models.AutoField(default='00', primary_key=True, serialize=False),
        ),
    ]
