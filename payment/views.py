from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from app.models import Payment



def getpaymentinfo(request):
    c={}
    c.update(csrf(request))
    return render_to_response('SalaryPayment.html', c)

def payment(request):
    payment_mode = request.POST.get('','')
    amount = request.POST.get('','')
    c={}
    c.update(csrf(request))
    pay = Payment(payment_mode=payment_mode,amount=amount)
    pay.save()
    return HttpResponseRedirect('/app/addsuccess/',c)


def addsuccess(request):
    c={}
    c.update(csrf(request))
    return render_to_response('/templates/index.html',c)

class HospitalListView(generic.ListView):
    model = Payment


