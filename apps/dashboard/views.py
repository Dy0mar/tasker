# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from dashboard.models import Task


@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
