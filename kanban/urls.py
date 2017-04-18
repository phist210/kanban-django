from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.edit_task, name='edit_task'),
    url(r'^(?P<id>[0-9]+)/delete', views.delete_task, name='delete_task'),
]
