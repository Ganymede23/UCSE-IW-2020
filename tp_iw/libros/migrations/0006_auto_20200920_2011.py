# Generated by Django 3.1 on 2020-09-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_auto_20200920_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(),
        ),
    ]