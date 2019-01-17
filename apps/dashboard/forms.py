# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from dashboard.models import Task, TaskLog


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True, author=False, user=False):
        data = None
        action = TaskLog.UPDATE_TASK

        task = super(TaskForm, self).save(commit=False)

        if not user:
            raise ValidationError('User was lost')

        if not task.author:  # Create task
            if author:
                action = TaskLog.CREATE_TASK
                task.author = author
            else:
                raise ValidationError('Author already exists')

        else:  # Update task
            origin = self.Meta.model.objects.get(pk=self.instance.pk)
            for field in self.cleaned_data:
                old_value = getattr(origin, field, None)
                new_value = self.cleaned_data.get(field)

                if old_value != new_value:
                    data[field] = [old_value, new_value]

        if commit:
            task.save()
            TaskLog.objects.create(
                action=action,
                task=task,
                data=data or None,
                user=user,
            )
        return task

    class Meta(object):
        model = Task
        fields = (
            'subject', 'status', 'assigned_to', 'time_estimate', 'body_text',
        )
