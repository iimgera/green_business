# Generated by Django 4.1.7 on 2023-04-07 05:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(help_text='Enter your content here.', verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(help_text='Enter your content here.', null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(help_text='Enter your content here.', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Контакты',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GeneralMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('sub_title_ru', models.CharField(max_length=150, null=True, verbose_name='Подзаголовок')),
                ('sub_title_en', models.CharField(max_length=150, null=True, verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Общая основная страница',
                'ordering': ['-id'],
            },
        ),
    ]