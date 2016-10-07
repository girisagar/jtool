from django.shortcuts import render
from desk.models import Task, TaskList
from desk.forms import TaskForm


from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView
)

from django.views.generic import ListView
from django.core.urlresolvers import reverse


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.task_list_id = self.kwargs['task_list_id']
        return super(TaskCreateView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self):
        return reverse("task_list", args=[self.kwargs['task_list_id']])


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task


class TaskListView(ListView):
    model = TaskList

    def get_queryset(self):
        return Task.objects.filter(task_list_id=self.kwargs['task_list_id'])

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['form'] = TaskForm()
        context['list'] = TaskList.objects.get(id=self.kwargs['task_list_id'])
        print context
        return context
