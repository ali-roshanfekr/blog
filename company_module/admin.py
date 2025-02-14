from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title']


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['title']


class RelatedImageAdmin(admin.ModelAdmin):
    list_display = ['paragraph']


admin.site.register(CompanyModel, CompanyAdmin)
admin.site.register(ParagraphModel, ParagraphAdmin)
admin.site.register(RelatedImageModel, RelatedImageAdmin)
