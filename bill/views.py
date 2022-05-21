from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt

def getpatientname(request):
    c={}
    c.update(csrf(request))
    return render_to_response('BillGeneration1.html',c)

def receptionist(request):
    c={}
    c.update(csrf(request))
    return render_to_response('receptionist.html',c)

def getupdateinfo(request):
    c={}
    c.update(csrf(request))
    return render_to_response('UpdateBill.html',c)

def getbillinfo(request):
    c={}
    c.update(csrf(request))
    patient_id=request.POST.get('p_id','')
    bb=Bill.objects.get(patient_id=patient_id)
    if bb is not None:
        app = Appointment.objects.get(patient_id=patient_id)
        p_name=app.patient_name
        p_id=app.patient_id
        med_bill=bb.medicine_bill
        others=bb.others
        total=med_bill+others
        request.session['tot']=total
        request.session['id']=p_id
        return render_to_response('BillGeneration2.html',{"p_name":p_name, "p_id":p_id, "med_bill":med_bill, "others":others, "total":total},c)
    else:
        return HttpResponseRedirect('/bill/getpatientname/',c)

def bill(request):
    patient_id = request.POST.get('p_id','')
    app = Appointment.objects.get(patient_id=patient_id)
    bb = Bill.objects.get(patient_id=patient_id)
    if bb is not None:
        c = {}
        c.update(csrf(request))
        medicine_bill =bb.medicine_bill+(int(request.POST.get('med_bill','')))
        others = bb.others+(int(request.POST.get('others','')))
        bb.medicine_bill=medicine_bill
        bb.others=others
        bb.save()
        return HttpResponseRedirect('/bill/reception/', c)
    else:
        medicine_bill = request.POST.get('med_bill', '')
        others = request.POST.get('others', '')
        c={}
        c.update(csrf(request))
        b = Bill(patient_id=app,medicine_bill=medicine_bill,others=others)
        b.save()
        return HttpResponseRedirect('/bill/reception/',c)

def payment(request):
    c = {}
    c.update(csrf(request))
    total=request.session['tot']
    return render_to_response('Payment.html',{'total':total},c)

def billpaid(request):
    c = {}
    c.update(csrf(request))
    b1=Bill.objects.get(patient_id=request.session['id'])
    b1.delete()
    return HttpResponseRedirect('/bill/reception/',c)

def addsuccess(request):
    c={}
    c.update(csrf(request))
    return render_to_response('myindex.html',c)

class HospitalListView(generic.ListView):
    model = Bill
