import jdatetime
from django.db import models


class MemoryModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='memory', verbose_name='تصویر')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    author = models.CharField(max_length=100, null=True, blank=True, verbose_name='نویسنده')

    def __str__(self):
        return self.title

    def get_date_fa(self):
        date_fa = jdatetime.GregorianToJalali(self.date.year, self.date.month, self.date.day)
        final_date = date_fa.getJalaliList()
        return f'{final_date[0]}/{final_date[1]}/{final_date[2]}'

    class Meta:
        verbose_name = 'خاطره'
        verbose_name_plural = 'خاطرات'


class MemoryParagraphModel(models.Model):
    memory = models.ForeignKey(MemoryModel, on_delete=models.CASCADE, related_name='paragraph', verbose_name='خاطره')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    quote = models.TextField(null=True, blank=True, verbose_name='نقل قول')

    def __str__(self):
        if self.title:
            return f'{self.memory.title} / {self.title}'

        else:
            return f'{self.memory.title} / {self.id}'

    class Meta:
        verbose_name = 'بند'
        verbose_name_plural = 'بند ها'


class MemoryRelatedImageModel(models.Model):
    paragraph = models.ForeignKey(MemoryParagraphModel, on_delete=models.CASCADE, related_name='images',
                                  verbose_name='بند')
    image = models.ImageField(upload_to='memory/related', verbose_name='تصویر')

    def __str__(self):
        return f'{self.paragraph.memory.title} / {self.paragraph.title}'

    class Meta:
        verbose_name = 'تصویر مرتبط'
        verbose_name_plural = 'تصاویر مرتبط'
