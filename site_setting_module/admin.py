from django.contrib import admin
from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ['name']


class DailyAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['title']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['title']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['link', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


class LogoAdmin(admin.ModelAdmin):
    list_display = ['id']


class BackGroundAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


admin.site.register(MainModel, MainAdmin)
admin.site.register(DailyModel, DailyAdmin)
admin.site.register(ServiceModel, ServiceAdmin)
admin.site.register(WorkModel, WorkAdmin)
admin.site.register(EducationModel, EducationAdmin)
admin.site.register(LinkModel, LinkAdmin)
admin.site.register(LogoModel, LogoAdmin)
admin.site.register(BackGroundModel, BackGroundAdmin)
