# Generated by Django 3.0.1 on 2020-03-27 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppvs', '0003_auto_20200326_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppv',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title that was defended'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of pay per view')),
                ('result', models.CharField(max_length=150, verbose_name='Result of match')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppvs.PPV')),
            ],
        ),
    ]
