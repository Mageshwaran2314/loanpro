# Generated by Django 3.0 on 2019-12-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20191218_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetails',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
