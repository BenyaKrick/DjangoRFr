# Generated by Django 4.2 on 2023-04-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=80, unique=True, verbose_name='Рубрика'),
        ),
    ]
