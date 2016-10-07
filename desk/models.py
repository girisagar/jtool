from __future__ import unicode_literals

from django.db import models

DEFAULT_STATUS = 1
DEFAULT_PRIORITY = 1


class Category(models.Model):
    name = models.CharField(max_length=20)


class Priority(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=25)


class Status(models.Model):
    name = models.CharField(max_length=15)
    css = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)


class Task(models.Model):
    text = models.CharField(max_length=120)
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey('TaskList')
    duedate = models.DateTimeField(null=True, blank=True)
    notify = models.BooleanField(default=True)
    status = models.ForeignKey(Status, null=True, blank=True)
    priority = models.ForeignKey(Priority, null=True, blank=True)


class TaskList(models.Model):
    name = models.CharField(max_length=50)

