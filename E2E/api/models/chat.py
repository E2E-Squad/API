from django.db import models


class Chat(models.Model):
    confirmed = models.BooleanField(default=False)
    requested_by = models.ForeignKey(
        'Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )
    reported_by = models.ForeignKey(
        'Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name="reported_chats",
    )


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        'Student',
        on_delete=models.SET_NULL
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )