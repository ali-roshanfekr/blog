# Generated by Django 5.1.5 on 2025-02-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
            ],
            options={
                'verbose_name': 'تحصیلات',
                'verbose_name_plural': 'تحصیلات',
            },
        ),
    ]
