from rest_framework import serializers

from .models import MessageInfo


class MessageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageInfo
        fields = ['user_id', 'chat_id', 'group_name', 'first_name', 'last_name', 'username',
                  'message_count', 'days_activity', 'last_date_activity']
