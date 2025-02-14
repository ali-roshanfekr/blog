# Generated by Django 5.1.5 on 2025-02-13 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='memory', verbose_name='تصویر')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'خاطره',
                'verbose_name_plural': 'خاطرات',
            },
        ),
        migrations.CreateModel(
            name='MemoryParagraphModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('quote', models.TextField(blank=True, null=True, verbose_name='نقل قول')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraph', to='memory_module.memorymodel', verbose_name='خاطره')),
            ],
            options={
                'verbose_name': 'بند',
                'verbose_name_plural': 'بند ها',
            },
        ),
        migrations.CreateModel(
            name='MemoryRelatedImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='memory/related', verbose_name='تصویر')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='memory_module.memoryparagraphmodel', verbose_name='بند')),
            ],
            options={
                'verbose_name': 'تصویر مرتبط',
                'verbose_name_plural': 'تصاویر مرتبط',
            },
        ),
    ]
