# Generated by Django 2.0.4 on 2018-04-27 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0006_auto_20180427_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voto',
            name='usuario_id',
        ),
    ]