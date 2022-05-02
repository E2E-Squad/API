from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_moderator = models.BooleanField('moderator status', default=False)


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'is_student': True}
    )
    parent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_student': False}
    )
    chats = models.ManyToManyField('Chat')
    blocked_list = models.ManyToManyField(User)
    need = models.ManyToManyField('Topic')
    offer = models.ManyToManyField('Topic')
