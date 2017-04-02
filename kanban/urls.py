from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^myaccount', views.myaccount, name='myaccount'),
    url(r'^new_task/', views.new_task, name='new_task'),

]
