# Generated by Django 3.0.1 on 2020-06-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0011_auto_20200629_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='info',
            field=models.TextField(blank=True, verbose_name='Info about title'),
        ),
    ]
