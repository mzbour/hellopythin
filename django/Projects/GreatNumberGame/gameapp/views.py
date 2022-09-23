from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
import random 
def show (request):
    request.session['randnum']=random.randint(1, 100)
    print(request.session['randnum'])
    request.session['mynum1']=-1
    context={
        'key1':request.session['randnum'],
        'key2':request.session['mynum1']
    }
    return render(request,"index.html",context=context)
    
def show1 (request):
    print(request.POST['num'])
    # if 'randnum' not in session:
    #     return render(request,'index.html')
   # request.session['randnum']=random.randint(1, 100)
    request.session['mynum1']=int(request.POST['num'])
    
    context={
        'key1':request.session['randnum'],
        'key2':request.session['mynum1']
    }
    print(context)
    # print(request.session['randnum'])
    return render(request,'index.html',context=context)



