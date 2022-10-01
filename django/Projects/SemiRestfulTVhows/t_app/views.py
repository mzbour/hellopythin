from multiprocessing import context
from django.shortcuts import render,redirect
from t_app.models import *
from django.contrib import messages
def show(request):
    context={"shows":Show.objects.all()}
    return render(request,'show.html',context)


def first(request):
    myid=(Show.objects.last()).id
    return redirect('/shows/'+str(myid))

def edit(request,showid):
    S1=Show.objects.get(id=showid)
    context={"s1":S1}
    return render(request,'edit.html',context)

def preedit(request,myid):
    errors = Show.objects.validate_show(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/'+str(myid)+'/edit')
    else:
     show1=Show.objects.get(id=myid)
     show1.title=request.POST['titleme']
     show1.network=request.POST['network']
     show1.relateddate=request.POST['date']
     show1.desc=request.POST['description']
     show1.save()
     return redirect('/')

def createshow(request):

   return render(request,'add.html')

def myproplem(request):
    Show.objects.create(title=request.POST['ta'],network=request.POST['na'],relateddate=request.POST['da'],desc=request.POST['descriptiona'])
    return redirect('/')

def tv(request,idm):
    context={"showtv":Show.objects.get(id=idm)}
    return render(request,'tv.html',context)


def returntotv(request,rid):
    redirect('shows/'+rid)

def delete(request,mid):
    s=Show.objects.get(id=mid)
    s.delete()
    return redirect('shows/')

























# def add(request):
#    my_ereor=Show.objects.validate_show(request.POST)
#    if len(errors)>0:

#    showm=Show.objects.create(title=request.POST['ta'],network=request.POST['na'],relateddate=request.POST['da'],desc=request.POST['descriptiona'])
#    context={
#     "addshow":showm
#     }
#    return render(request,'add.html')
#      return redirect('shows/'+showm.id)
