from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
# path('', views.index, name='index'),
    path('getpatientinfo/', views.getpatientinfo),
    path('Appointment/', views.appointment),
    path('addsuccess/', views.addsuccess),
    path('appointment/', views.HospitalListView.as_view(), name = 'appointment'),
]