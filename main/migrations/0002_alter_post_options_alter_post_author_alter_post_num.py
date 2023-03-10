# Generated by Django 4.1.7 on 2023-02-16 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['time_create'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='num',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Артикль'),
        ),
    ]
