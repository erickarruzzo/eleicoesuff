# Generated by Django 2.0.4 on 2018-06-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0029_auto_20180528_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='votos_recebidos',
            field=models.IntegerField(default=0),
        ),
    ]
