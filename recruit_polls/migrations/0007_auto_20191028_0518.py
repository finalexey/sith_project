# Generated by Django 2.2.6 on 2019-10-28 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0011_auto_20191023_2230'),
        ('recruit_polls', '0006_auto_20191028_0342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Check',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='recruit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Recruit'),
        ),
    ]
