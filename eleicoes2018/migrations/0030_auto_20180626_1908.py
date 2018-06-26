# Generated by Django 2.0.4 on 2018-06-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0029_auto_20180528_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoCargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('salario', models.FloatField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes2018.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='LocalVotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.IntegerField()),
                ('secao', models.IntegerField()),
                ('local', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='total_votos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estado',
            name='total_eleitores',
            field=models.IntegerField(default=5000000),
        ),
        migrations.AddField(
            model_name='noticia',
            name='candidato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicoes2018.Candidato'),
        ),
        migrations.AddField(
            model_name='localvotacao',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes2018.Estado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='local_votacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicoes2018.LocalVotacao'),
        ),
    ]