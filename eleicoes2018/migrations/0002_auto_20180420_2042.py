# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidato_id', models.ForeignKey(to='eleicoes2018.Candidato', on_delete=models.PROTECT)),
                ('cargo_id', models.ForeignKey(to='eleicoes2018.Cargo', on_delete=models.PROTECT)),
                ('usuario_id', models.ForeignKey(to='eleicoes2018.Usuario',on_delete=models.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='candidato',
            name='cargo_id',
            field=models.ForeignKey(to='eleicoes2018.Cargo', on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='estado_id',
            field=models.ForeignKey(to='eleicoes2018.Estado',on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido_id',
            field=models.ForeignKey(to='eleicoes2018.Partido', on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(default=datetime.datetime(2018, 4, 20, 20, 42, 8, 226923, tzinfo=utc), max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado_id',
            field=models.ForeignKey(default=1, to='eleicoes2018.Estado', on_delete=models.PROTECT),
            preserve_default=False,
        ),
    ]
