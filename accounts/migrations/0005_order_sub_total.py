# Generated by Django 3.0.6 on 2020-10-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
