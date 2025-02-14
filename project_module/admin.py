from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['title']


class RelatedImageAdmin(admin.ModelAdmin):
    list_display = ['paragraph']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ProjectModel, ProjectAdmin)
admin.site.register(ParagraphModel, ParagraphAdmin)
admin.site.register(RelatedImageModel, RelatedImageAdmin)
admin.site.register(TagModel, TagAdmin)
