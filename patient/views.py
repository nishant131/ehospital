# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from app.models import *

def getpatientinfo(request):
    c={}
    c.update(csrf(request))
    return render_to_response('Appointment.html', c)

def appointment(request):
    patient_id = request.POST.get('patient_id','')
    patient_name = request.POST.get('patient_name','')
    patient_age = request.POST.get('patient_age','')
    patient_address = request.POST.get('patient_address','')
    date = request.POST.get('date','')
    doctor = request.POST.get('doctor','')
    c={}
    c.update(csrf(request))
    a=Appointment(patient_id=patient_id,patient_name=patient_name,patient_age=patient_age,patient_address=patient_address,date=date,doctor=doctor)
    bb=Bill(patient_id=a,medicine_bill=0,others=0)
    a.save()
    bb.save()
    return render_to_response('receptionist.html', c)


def addsuccess(request):
    c={}
    c.update(csrf(request))
    return render_to_response('index.html', c)

class HospitalListView(generic.ListView):
    model = Appointment
