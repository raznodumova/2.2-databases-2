# Generated by Django 3.1.2 on 2024-11-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20241105_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]