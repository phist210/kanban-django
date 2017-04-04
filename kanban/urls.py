from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^myaccount', views.myaccount, name='myaccount'),
    # url(r'^new_task/', views.new_task, name='new_task'),
<<<<<<< HEAD
=======
    # url(r'^inplaceeditform/', include('inplaceeditform.urls')),
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed

]
