from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime
def display1(request):
    context = {
         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
              }
    return render(request,"index1.html",context)

def display2(request):
    # if request.method=='POST':
    #         list_from_form = request.POST['mylist']
    #         language_from_form=request.POST['mylanguage']
    #         mycomments_from_form=request.POST['mycomments']
    #         yourname_from_form=request.POST['yourname']
    #   return render('/display1/display2')      
      return render(request,"index2.html")

def display3(request):
    list_from_form = request.POST['mylist']
    language_from_form=request.POST['mylanguage']
    mycomments_from_form=request.POST['mycomments']
    yourname_from_form=request.POST['yourname']
    context={
      "yourname_from_context":yourname_from_form,  
      "mycomments_from_context":mycomments_from_form,
      "list_from_context":list_from_form,
      " language_from_context": language_from_form
    }
    return render(request,"index3.html",context)
    

# def create_user(request):
#     print("Got Post Info....................")
#     name_from_form = request.POST['name']
#     email_from_form = request.POST['email']
#     context = {
#     	"name_on_template" : name_from_form,
#     	"email_on_template" : email_from_form
#     }
#     return render(request,"show.html",context)
# from django.shortcuts import render
# from time import gmtime, strftime
    
# def display1(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request,'index.html', context)

# from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "GET":
        print(request.GET)
        return render(request, "index1.html")
    	

    if request.method == "POST":
        print(request.POST)
        return redirect("/")


# def some_function(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	val_from_field_two = request.POST["two"]
