# Generated by Django 2.0.4 on 2018-05-08 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0012_remove_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voto',
            name='cargo_id',
        ),
    ]
