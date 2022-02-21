# Generated by Django 3.0.1 on 2020-03-27 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppvs', '0010_remove_title_ppv'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='ppv',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ppvs.PPV'),
            preserve_default=False,
        ),
    ]
