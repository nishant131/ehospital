# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from app.models import *

def getemployeeinfo(request):
    c={}
    c.update(csrf(request))
    return render_to_response('Registration.html', c)

def Registration(request):
    e_id = request.POST.get('Employee_Id', '')
    e_password = request.POST.get('pwd', '')
    e_repassword = request.POST.get('rpwd','')
    e_name = request.POST.get('Name', '')
    email = request.POST.get('Email_Address', '')
    age = request.POST.get('Age', '')
    Mobile_no = request.POST.get('Mobile_No', '')
    e_address = request.POST.get('Address', '')
    e_type = request.POST.get('Employee_Type', '')

    '''ss=Employee.objects.get(e_id="sss")'''

    c={}
    c.update(csrf(request))
    if e_password != e_repassword:
        c['s'] = "password and repassword are not match"
        return render_to_response('/app/getemployeeinfo', c)

    else:
        e = Employee(e_id=e_id, e_password=e_password, e_name=e_name, email=email, age=age, Mobile_no=Mobile_no, e_address=e_address,e_type=e_type)
        e.save()
        user = User.objects.create_user(username=e_id, password=e_password)
        user.save()
        return HttpResponseRedirect('/app/addsuccess/', c)

def addsuccess(request):
    c={}
    c.update(csrf(request))
    return render_to_response('index.html', c)

class HospitalListView(generic.ListView):
    model = Employee
