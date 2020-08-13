from django.contrib import admin
import django.contrib.auth.views
from django.urls import path

import django_otp.views

import otp_agents.views

from . import views


urlpatterns = [
    path('login/', django.contrib.auth.views.LoginView.as_view()),
    path('verify/', django_otp.views.LoginView.as_view()),
    path('trust/', otp_agents.views.LoginView.as_view()),
    path('logout/', django.contrib.auth.views.LogoutView.as_view()),

    path('otp/', views.otp_view),
    path('otp2/', views.otp_view_2),
    path('otp_advised/', views.otp_advised_view),
    path('otp_advised_2/', views.otp_advised_view_2),
    path('agent/', views.agent_view),

    path('admin/', admin.site.urls),
]
