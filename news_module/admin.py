from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_date_fa']


class NewsParagraphAdmin(admin.ModelAdmin):
    list_display = ['title']


class NewsRelatedImageAdmin(admin.ModelAdmin):
    list_display = ['paragraph']


admin.site.register(NewsModel, NewsAdmin)
admin.site.register(NewsParagraphModel, NewsParagraphAdmin)
admin.site.register(NewsRelatedImageModel, NewsRelatedImageAdmin)
