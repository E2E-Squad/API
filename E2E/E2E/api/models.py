from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Conversation(models.Model):
    user1 = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="participate1",
    )
    user2 = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="participate2",
    )
    blocked_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blocked",
    )

class Meeting(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        null=True,
        on_delete=models.SET_NULL,
    )
    date = models.DateTimeField()
    bidirectional = models.BooleanField()
    helper = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

class Grade(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        null=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

