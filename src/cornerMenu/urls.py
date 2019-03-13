"""cornerMenu URL Configuration

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
from django.conf.urls import url
#from django.urls import  path
from django.contrib import admin

from home.views import (HomeView)
from menu.views import (MenuCreateView,MenuListView,MenuDelete,MenuUpdateView,SendToSlack)
from menuCreate.views import (MenuCreateList,MenuCreateRegister,MenuCreateDelete)
from menuResponse.views import (MenuResponseRegister)

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^home/', HomeView.as_view(), name='home'),

    url(r'^$', HomeView.as_view()),

    url(r'^menu/create/', MenuCreateView.as_view(), name="menucreate"),    
    url(r'^menu/create/(?P<id>[0-9a-f-]+)/$', MenuCreateView.as_view(), name="menucreateparams"),
    url(r'^menulist/', MenuListView.as_view(), name="menulist"),
    url(r'^menu/(?P<pk>[0-9]+)/delete/$', MenuDelete.as_view(), name='delete'),
    url(r'^menu/(?P<pk>[0-9]+)/$', MenuUpdateView.as_view(), name='update'),

    url(r'^menuCreatelist/', MenuCreateList.as_view(), name="menucreatelist"),    
    url(r'^menuCreate/create', MenuCreateRegister.as_view()),
    url(r'^menuCreate/(?P<pk>[0-9a-f-]+)/delete/$', MenuCreateDelete.as_view(), name='deletemenucreate'),

    url(r'^menuResponse/menu/(?P<id>[0-9a-f-]+)/(?P<user>[a-zA-Z0-9!@#$&()=]+)/$', MenuResponseRegister.as_view(), name="menuresponsecreate"),

    url(r'^menu/SendToSlack/(?P<id>[0-9a-f-]+)/$', SendToSlack.as_view(), name='sendtoslack'),
]
