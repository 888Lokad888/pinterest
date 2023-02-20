# Generated by Django 4.1.7 on 2023-02-17 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_post_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Добавлено пользователем'),
        ),
    ]
