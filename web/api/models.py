from django.db import models


class MessageInfo(models.Model):
    user_id = models.IntegerField()
    chat_id = models.IntegerField()
    group_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    message_count = models.IntegerField(default=0, blank=True, null=True)
    days_activity = models.IntegerField()
    last_date_activity = models.DateField()
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'api_message_info'
        unique_together = ['user_id', 'chat_id']

    def __str__(self):
        msg = f'{self.username} | {self.user_id} | {self.chat_id} | {self.group_name}'

        return msg
