# Generated by Django 4.2.2 on 2023-07-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_article_id_article_article_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]