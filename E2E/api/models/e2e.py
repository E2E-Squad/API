from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .users import Student


class Chat(models.Model):
    confirmed = models.BooleanField(default=False)
    requested_by = models.ForeignKey(
        Student,
        null=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )
    reported_by = models.ForeignKey(
        Student,
        null=True,
        on_delete=models.SET_NULL,
        related_name="reported_chats",
    )


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )


class Meeting(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    bidirectional = models.BooleanField()
    helper = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )


class Grade(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        null=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
