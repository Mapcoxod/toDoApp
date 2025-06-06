# Generated by Django 5.2.1 on 2025-05-25 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='дата обновления')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('completed', models.BooleanField(default=False, verbose_name='выполнено')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
                'ordering': ['-created_at'],
            },
        ),
    ]
