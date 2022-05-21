from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
# path('', views.index, name='index'),
    path('getemployeeinfo/', views.getemployeeinfo),
    path('Registration/', views.Registration),
    path('addsuccess/', views.addsuccess),
    path('employee/', views.HospitalListView.as_view(), name='employee'),


]