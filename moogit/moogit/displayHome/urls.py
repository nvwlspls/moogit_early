# Author: Wayne Jessen
# Description: This file contains urls for the RaliG application
# 
# Version. 1.0


from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'displayHome.views.homePage', name = 'home'),
    )