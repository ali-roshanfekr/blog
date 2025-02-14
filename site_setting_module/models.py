from django.db import models


class MainModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    image = models.ImageField(upload_to='main', verbose_name='تصویر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پروفایل کارفرما'
        verbose_name_plural = 'پروفایل کارفرما'


class DailyModel(models.Model):
    text = models.TextField(verbose_name='متن')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'روزنوشت'
        verbose_name_plural = 'روزنوشت ها'


class ServiceModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(null=True, blank=True, verbose_name='متن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'


class WorkModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(null=True, blank=True, verbose_name='متن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کار ها'


class EducationModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(null=True, blank=True, verbose_name='متن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تحصیلات'
        verbose_name_plural = 'تحصیلات'


class LinkModel(models.Model):
    link = models.CharField(max_length=200, verbose_name='لینک')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان: اگر آیکون دارد خالی بگذارید')
    icon = models.CharField(max_length=100, null=True, blank=True, verbose_name='آیکون')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک ها'


class LogoModel(models.Model):
    image = models.ImageField(upload_to='logo', verbose_name='لوگو')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'لوگو'
        verbose_name_plural = 'لوگو'


class BackGroundModel(models.Model):
    image = models.ImageField(upload_to='back_ground', verbose_name='پس زمینه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'پس زمینه'
        verbose_name_plural = 'پس زمینه ها'
