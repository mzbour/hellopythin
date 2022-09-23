from django.shortcuts import render
def display1(request):
   return render(request,"index.html")

def display2(request):
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
    return render(request,"index2.html",context)