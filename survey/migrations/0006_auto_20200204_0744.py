# Generated by Django 3.0.3 on 2020-02-04 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20190603_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'permissions': (('view_results', 'View survey results'),)},
        ),
    ]
