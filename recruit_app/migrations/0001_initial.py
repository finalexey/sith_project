# Generated by Django 2.2.6 on 2019-10-17 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название планеты')),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя Ситха')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя Рекрута')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_accepted', models.BooleanField(verbose_name='Принят ли рекрут')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.Planet')),
            ],
        ),
    ]