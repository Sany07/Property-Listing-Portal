# Generated by Django 3.0.7 on 2020-06-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20200626_1733'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='listing',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Property', to='listing.Property'),
            preserve_default=False,
        ),
    ]