# Generated by Django 2.1.15 on 2020-05-29 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0003_code_show_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='show_name',
        ),
    ]