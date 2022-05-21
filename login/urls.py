from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.login),
    path('auth/', views.auth_view),
]
