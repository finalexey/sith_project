# Generated by Django 2.2.6 on 2019-10-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0002_auto_20191020_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='Принят ли рекрут'),
            preserve_default=False,
        ),
    ]