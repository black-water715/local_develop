# Generated by Django 3.2.19 on 2023-08-25 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка новости')),
                ('news_text', models.TextField(verbose_name='Текст новости')),
                ('news_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации новости')),
                ('news_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата комментария')),
                ('comment_author', models.ForeignKey(db_column='comment_author', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('news', models.ForeignKey(db_column='news', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddConstraint(
            model_name='news',
            constraint=models.UniqueConstraint(fields=('id', 'news_author'), name='unique_news_title'),
        ),
    ]
