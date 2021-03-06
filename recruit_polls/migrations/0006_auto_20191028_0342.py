# Generated by Django 2.2.6 on 2019-10-28 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruit_polls', '0005_auto_20191024_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False, help_text='Все вопросы пройдены', verbose_name='Все вопросы пройдены')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruit_polls.Choice'),
        ),
    ]
