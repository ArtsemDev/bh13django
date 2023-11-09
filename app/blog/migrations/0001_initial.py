# Generated by Django 4.2.7 on 2023-11-09 17:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('descr', models.TextField(verbose_name='описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликовано')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ['category', 'title'],
            },
        ),
    ]
