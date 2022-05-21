from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from app.models import *

def viewappointment(request):
    c={}
    c.update(csrf(request))
    doc=request.session['name']
    app=Appointment.objects.filter(doctor=doc)
    return render_to_response('ViewAppointment.html',{"app":app,"doc":doc})
