from django.conf.urls import url

from desk.views import(
   TaskCreateView,
   TaskUpdateView,
   TaskDeleteView,
   TaskListView
)


urlpatterns = [
    url(r'^(?P<task_list_id>\d+)/$', TaskListView.as_view(), name='task_list'),
    url(r'^(?P<task_list_id>\d+)/list/$', TaskListView.as_view(), name='task_list'),
    url(r'^(?P<task_list_id>\d+)/create/$', TaskCreateView.as_view(), name='task_create'),
    url(r'^update/(?P<pk>\d+)/$', TaskUpdateView.as_view(), name='task_update'),
    url(r'^delete/(?P<pk>\d+)/$', TaskDeleteView.as_view(), name='task_delete'),
]
