# Generated by Django 3.1 on 2020-10-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escritos', '0024_auto_20201009_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denuncia',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='denuncia',
            name='motivo',
        ),
        migrations.RemoveField(
            model_name='denuncia',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Denuncia',
        ),
        migrations.DeleteModel(
            name='MotivoDenuncia',
        ),
    ]