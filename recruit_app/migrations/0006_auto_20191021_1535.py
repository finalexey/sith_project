# Generated by Django 2.2.6 on 2019-10-21 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0005_auto_20191020_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sithname',
            name='sith_name',
        ),
        migrations.AddField(
            model_name='sithname',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='Имя Ситха'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.SithName', verbose_name='Имя ситха'),
        ),
    ]
