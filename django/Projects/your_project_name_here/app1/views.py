from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return HttpResponse('hello')

# def numme(request):
#     return HttpResponse('my number is mohamamd al bzour')
    
ll=["blog1","blog2","blog3"]
def root(request):

    return HttpResponse(ll)
def indexm(request):
    return HttpResponse("placeholder to later display a list of all blogs" )
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
# def new(request):
#     ll.append("newPlock")
#     return HttpResponse(ll)
def create(requrst):
    return redirect('/blogs')
    # return HttpResponse("The new Bolk will added")

def  edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def show (request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def destroy(request):
     return redirect('blogs/')

def index1(request):
    return render('index.html')

def numme(request,name):
    context={
        "htmlname":name,
        "nameist":["mohamamd","ali","ahmed"]
    }
    return render(request,"index.html",context)

