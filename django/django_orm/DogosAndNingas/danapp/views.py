from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *


def showme(request):
     
      context = {
    	"all_of_dojos": Dojo.objects.all(),"all_of_ninjas":Ninja.objects.all()
    }
      print(context)
      return render(request, "DojoAndNinja.html", context)


def hello(request):
    if request.POST['add1'] == 'add_dojo':
        Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return redirect('/')
    if request.POST['add1'] == 'add_ninja':
        dojoobject=request.POST['select1']
        dojo1 = Dojo.objects.get(name=dojoobject)
        Ninja.objects.create(first_namerequest.POST['first_name'],dojo=dojo1,last_name=request.POST['last_name'])
    return redirect('/')


    
