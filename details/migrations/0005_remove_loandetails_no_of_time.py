# Generated by Django 3.0 on 2019-12-18 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_loandetails_no_of_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loandetails',
            name='no_of_time',
        ),
    ]
