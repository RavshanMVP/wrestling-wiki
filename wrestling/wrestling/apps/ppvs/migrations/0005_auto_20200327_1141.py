# Generated by Django 3.0.1 on 2020-03-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppvs', '0004_auto_20200327_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ppv',
            name='title',
        ),
        migrations.AlterField(
            model_name='matches',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title that was defended'),
        ),
    ]
