# Generated by Django 2.2.6 on 2019-10-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0009_auto_20191021_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Планета'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='Принят ли рекрут'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Имя Рекрута'),
        ),
    ]
