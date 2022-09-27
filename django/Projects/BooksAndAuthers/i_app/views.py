from multiprocessing import context
from django.shortcuts import render,redirect
from i_app.models import Author, Book
def showbook(request):
    context={"bookm":Book.objects.all()}
    return render(request,'showbook.html',context)

def showauthor(request):
    context={"authorm":Author.objects.all()}
    return render(request,'showauthor.html',context)


def bookpage(request,idbook):
#    idid=int(idbook)
   context={"bookh":Book.objects.get(id=idbook)}
   return render(request,'bookpage.html',context)


def authorpage(request,idauthor):
    context={"authorh":Author.objects.get(id=idauthor)}
    
    return render(request,'authorpage.html',context)

def addbook(request):
    Book.objects.create(title=request.POST['title'] ,desc=request.POST['mycontents'])
    return redirect('/')


def addauthor(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],nots=request.POST['mynots'] )
    return redirect('/authors')

    

