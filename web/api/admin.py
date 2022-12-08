from django.contrib import admin

from .models import MessageInfo

admin.site.site_header = 'Bot Web Admin'


@admin.register(MessageInfo)
class MessageInfoAdmin(admin.ModelAdmin):
    list_filter = ['user_id', 'chat_id']
