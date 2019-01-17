"""boockify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from dashboard import views

urlpatterns = [
    # dashboard
    path(r'create-task/', views.CreateTaskView.as_view(), name='create-task'),
    re_path(
        r'^update-task/(?P<pk>\d+)/$',
        views.UpdateTaskView.as_view(),
        name='update-task'
    ),
    re_path(
        r'^delete-task/(?P<pk>\d+)/$',
        views.DeleteTaskView.as_view(),
        name='delete-task'
    ),
    re_path(
        r'log-task/(?P<pk>\d+)/$',
        views.TaskLogTemplateDetail.as_view(),
        name='log-task'
    ),
    path(r'', views.TaskListView.as_view(), name='home'),
]
