"""kanban_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from kanban import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet, 'task-list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^kanban/', include('kanban.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(
        regex=r'^login/$',
        view=login,
        kwargs={'template_name': 'kanban/registration/login.html'},
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=logout,
        kwargs={'next_page': '/login'},
        name='logout'
    ),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
