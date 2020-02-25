# Generated by Django 2.2.6 on 2019-10-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0011_auto_20191023_2230'),
        ('recruit_polls', '0003_auto_20191023_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='recruit',
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_polls.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_polls.Question')),
                ('recruit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Recruit')),
            ],
        ),
    ]
