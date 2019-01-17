# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from dashboard.forms import TaskForm
from dashboard.models import Task


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
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.save(author=user, user=user)
        return redirect(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        return context


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.save(user=user)
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
