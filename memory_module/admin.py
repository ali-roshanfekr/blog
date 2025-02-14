from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class MemoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_date_fa']


class MemoryParagraphAdmin(admin.ModelAdmin):
    list_display = ['title']


class MemoryRelatedImageAdmin(admin.ModelAdmin):
    list_display = ['paragraph']


admin.site.register(MemoryModel, MemoryAdmin)
admin.site.register(MemoryParagraphModel, MemoryParagraphAdmin)
admin.site.register(MemoryRelatedImageModel, MemoryRelatedImageAdmin)
