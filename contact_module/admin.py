from django.contrib import admin
from .models import *
from jalali_date.admin import ModelAdminJalaliMixin


class MessageAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'get_date_fa']
    list_filter = ['sent_at', 'reply', 'user']


admin.site.register(MessageModel, MessageAdmin)
