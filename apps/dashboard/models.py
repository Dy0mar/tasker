from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3
    CHOICE_STATUS = (
        (TODO, 'TODO'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (DONE, 'DONE'),
    )

    subject = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, choices=CHOICE_STATUS, default=TODO
    )
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='author'
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='assigned_to'
    )
    time_estimate = models.FloatField(null=True, blank=True, default=None)
    time_spent = models.FloatField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class TaskLog(models.Model):
    CREATE_TASK = 'CREATE_TASK'
    UPDATE_TASK = 'EDIT_TASK'
    DELETE_TASK = 'DELETE_TASK'

    ACTIONS = (
        (CREATE_TASK, 'CREATE TASK'),
        (UPDATE_TASK, 'UPDATE TASK'),
        (DELETE_TASK, 'DELETE TASK'),
    )
    action = models.CharField(max_length=255, choices=ACTIONS)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL,
                             blank=True, null=True)
    data = JSONField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
