from django.db import models


class TagModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class ProjectModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='product', verbose_name='تصویر')
    tag = models.ManyToManyField(TagModel, blank=True, verbose_name='تگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اختراع'
        verbose_name_plural = 'اختراعات'


class ParagraphModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='paragraph', verbose_name='اختراع')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')

    def __str__(self):
        return f'{self.project.title} / {self.title}'

    class Meta:
        verbose_name = 'بند'
        verbose_name_plural = 'بند ها'


class RelatedImageModel(models.Model):
    paragraph = models.ForeignKey(ParagraphModel, on_delete=models.CASCADE, related_name='images', verbose_name='بند')
    image = models.ImageField(upload_to='product/related', verbose_name='تصویر')

    def __str__(self):
        return f'{self.paragraph.project.title} / {self.paragraph.title}'

    class Meta:
        verbose_name = 'تصویر مرتبط'
        verbose_name_plural = 'تصاویر مرتبط'
