# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView

from dashboard.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['new_tasks'] = Task.objects.filter(status=Task.TODO)
        context['in_progress_tasks'] = Task.objects.filter(
            status=Task.IN_PROGRESS
        )
        context['done_tasks'] = Task.objects.filter(status=Task.TODO)

        return context
