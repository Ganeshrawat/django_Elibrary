# Generated by Django 3.0.3 on 2020-03-15 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='price',
        ),
    ]
