# Generated by Django 2.2.6 on 2019-10-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruit',
            name='is_accepted',
        ),
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Планета'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Planet', verbose_name='Планета'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Planet', verbose_name='Планета'),
        ),
    ]