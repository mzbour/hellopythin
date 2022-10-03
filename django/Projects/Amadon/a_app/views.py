from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
my_account=1000
def index(request):
    return redirect('/amadon')

def amadon(request):
    return render(request,'a.html')


def buy(reauest):
    if request.POST['product_id'] =='19':
        context={
           "prise":19.99,"quantity":int(request.POST['quantity']),"spent":19.99*int(request.POST['quantity'])
        }
        return render(request,'show.html',context)
    
    if request.POST['product_id']=='29':
        context={
           "prise":29.99,"quantity":int(request.POST['quantity']),"spent":29.99*int(request.POST['quantity'])
        }
        return render(request,'show.html',context)
    if request.POST['product_id']=='4':
        context={
           "prise":4.99,"quantity":int(request.POST['quantity']),"spent":4.99*int(request.POST['quantity'])
        }
        return render(request,'show.html',context)
    if request.POST['product_id']=='49':
        context={
           "prise":49.99,"quantity":int(request.POST['quantity']),"spent":49.99*int(request.POST['quantity'])
        }
        return render(request,'show.html',context)  

# def red(reques):
#     return redirect('/amadon/buy')
# def show(request):
#     context={

#     }
#     return render(request,show.html,context)
