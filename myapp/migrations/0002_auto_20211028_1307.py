# Generated by Django 3.2.7 on 2021-10-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicsiteinfo',
            name='headerlink',
            field=models.CharField(default='', max_length=255, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='basicsiteinfo',
            name='headertitle',
            field=models.CharField(default='', max_length=100, verbose_name='LinkTitle'),
        ),
    ]