# Generated by Django 3.0.7 on 2020-06-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
