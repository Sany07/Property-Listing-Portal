# Generated by Django 3.0.7 on 2020-06-27 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_siteconfiguration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteConfiguration',
        ),
    ]