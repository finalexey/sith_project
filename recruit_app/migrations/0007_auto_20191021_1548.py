# Generated by Django 2.2.6 on 2019-10-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0006_auto_20191021_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Имя Ситха'),
        ),
        migrations.DeleteModel(
            name='SithName',
        ),
    ]
