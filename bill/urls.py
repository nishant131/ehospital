from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
# path('', views.index, name='index'),
    path('getpatientname/',views.getpatientname),
    path('getupdateinfo/',views.getupdateinfo),
    path('getbillinfo/',views.getbillinfo),
    path('update/',views.bill),
    path('addsuccess/',views.addsuccess),
    path('patient/', views.HospitalListView.as_view(), name = 'bill'),
    path('reception/',views.receptionist),
    path('payment/',views.payment),
    path('billpaid/',views.billpaid),
]