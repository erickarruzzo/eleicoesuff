# Generated by Django 2.0.4 on 2018-04-27 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicoes2018', '0005_auto_20180427_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]