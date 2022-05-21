from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from app.models import *
# Create your views here.

#class HomePageView(TemplateView):
#	def get(self, request, **kwargs):
#		return render(request, 'index.html', context=None)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('Employee_Id', '')
    password = request.POST.get('pwd', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        emp=Employee.objects.get(e_id=username)
        e_type=emp.e_type
        if e_type=="Receptionist":
            return render_to_response('receptionist.html')
        elif e_type=="Doctor":
            doc=emp.e_name
            request.session['name']=doc
            return render_to_response('doctor.html',{"doc":doc})
        else:
            return render_to_response('index.html')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')

@login_required(login_url = '/viewtest/login/')

def invalidlogin(request):
    return render_to_response('login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


