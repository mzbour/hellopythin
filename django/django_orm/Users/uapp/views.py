from multiprocessing import context
from django.shortcuts import render,redirect
from .models import User
def index(request):
     

      context = {
    	"all_the_users": User.objects.all()
    }
      print(context)
      return render(request, "index.html", context)


def index1(request):
    User.objects.create(first_name=request.POST['ffname'],last_name=request.POST['llname'],email=request.POST['eemail'] ,age=int(request.POST['aage']),created_at="",updated_at="")
    # User.objects.create(first_name=request.POST['ffname'],last_name=request.POST['llname'],email=request.POST['eemail'] ,age=int(request.POST['aage']),created_at="",updated_at="")

    return redirect('/')