# Generated by Django 3.2 on 2021-06-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_auto_20210602_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.IntegerField(default=27),
        ),
    ]