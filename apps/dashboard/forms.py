# -*- coding: utf-8 -*-

from django import forms
from dashboard.models import Task


class CreateTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta(object):
        model = Task
        fields = (
            'subject', 'status', 'assigned_to', 'time_estimate', 'body_text',
        )
