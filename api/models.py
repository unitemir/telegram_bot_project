from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    telegram_token = models.CharField(max_length=255, blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_user_permissions')


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

