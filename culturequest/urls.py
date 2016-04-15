"""culturequest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from main import views
#from main.views import api_root
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quest/$', views.QuestList.as_view()),
    url(r'^quest/(?P<pk>[0-9]+)/$', views.QuestDetail.as_view()),
    url(r'^question/$', views.QuestionList.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
    url(r'^location/$', views.LocationList.as_view()),
    url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    url(r'^gm/$', views.GmList.as_view()),
    url(r'^gm/(?P<pk>[0-9]+)/$', views.GmDetail.as_view()),
    url(r'^answer/$', views.AnswerList.as_view()),
    url(r'^answer/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view()),
   # url(r'^$', api_root.as_view()),
]
