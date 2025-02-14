from django.db import models


class CompanyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='product', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'


class ParagraphModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='paragraph', verbose_name='شرکت')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')

    def __str__(self):
        return f'{self.company.title} / {self.title}'

    class Meta:
        verbose_name = 'بند'
        verbose_name_plural = 'بند ها'


class RelatedImageModel(models.Model):
    paragraph = models.ForeignKey(ParagraphModel, on_delete=models.CASCADE, related_name='images', verbose_name='بند')
    image = models.ImageField(upload_to='product/related', verbose_name='تصویر')

    def __str__(self):
        return f'{self.paragraph.company.title} / {self.paragraph.title}'

    class Meta:
        verbose_name = 'تصویر مرتبط'
        verbose_name_plural = 'تصاویر مرتبط'
