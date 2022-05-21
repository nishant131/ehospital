from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
# path('', views.index, name='index'),
    path('getpaymentinfo/',views.getpaymentinfo),
    path('payment/',views.payment),
    path('addsuccess/',views.addsuccess),

    path('patient/', views.HospitalListView.as_view(), name = 'bill'),
]

