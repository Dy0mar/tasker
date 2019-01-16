# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView

from dashboard.forms import CreateTaskForm
from dashboard.models import Task, TaskLog


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        new_tasks = in_progress_tasks = done_tasks = 0
        for task in self.model.objects.all():
            if task.status == self.model.TODO:
                new_tasks += 1
            if task.status == self.model.IN_PROGRESS:
                in_progress_tasks += 1
            if task.status == self.model.DONE:
                done_tasks += 1

        context['new_tasks'] = new_tasks
        context['in_progress_tasks'] = in_progress_tasks
        context['done_tasks'] = done_tasks

        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/task_create.html'
    model = Task
    form_class = CreateTaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        TaskLog.objects.create(
            action=TaskLog.CREATE_TASK,
            task=task,
            data=None,
            user=self.request.user,
        )
        return redirect('home')

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        return context
