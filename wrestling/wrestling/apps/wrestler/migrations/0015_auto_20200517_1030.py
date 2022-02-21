# Generated by Django 3.0.1 on 2020-05-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrestler', '0014_wrestler_finisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrestler',
            name='cash_in',
            field=models.TextField(blank=True, verbose_name='Money in the bank cash in'),
        ),
        migrations.AddField(
            model_name='wrestler',
            name='rr_wm',
            field=models.TextField(blank=True, verbose_name='Royal Rumble winner at Wrestlemania'),
        ),
    ]
