# -*- coding: utf-8 -*-

from django.urls import path,reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns=[
    path("",views.index,name="homepage"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    ]

urlpatterns+=staticfiles_urlpatterns()
