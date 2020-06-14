# Generated by Django 3.0.7 on 2020-06-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('imgs', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description_short', models.CharField(max_length=600, verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Описание')),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]