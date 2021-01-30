from django.contrib import admin

from .models import Record, Comment


class RecordAdmin(admin.ModelAdmin):
    search_fields = ['song_title']

admin.site.register(Record, RecordAdmin)
# Register your models here.
admin.site.register(Comment)
