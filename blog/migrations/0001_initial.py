# Generated by Django 5.0.6 on 2024-07-24 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='Ссылка')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
