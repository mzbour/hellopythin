from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *
from django.contrib import messages
import urllib.request
		# path('', views.index),
        # path('reg_validate', views.reg_validate),
		# path('login_validate', views.login_validate),
		# path('home', views.home),
		# path('logout', views.logout)

def index(request):
 
    # if 'user' not in request.session:
    #     request.session['user'] = False
    
    return render(request, 'login.html')

def reg_validate(request):
    e = User.objects.reg_validation(request.POST)
    if len(e) > 0:
        for key, value in e.items():
            messages.error(request, value)
        return redirect('/')
    else:
        my_hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = my_hashed)
        # request.session['user']=request.POST['first_name']
        messages.success(request, 'You have registered succesfully ,Thank you and welcome to this our web')
        return redirect('/')

    
    # check = User.objects.filter(email = request.POST['email'])
    # error = False

    # if len(request.POST['first_name'])< 3:
    #     messages.error(request,'First Name must at laest contain two characters!', extra_tags = 'fn_error' )
    #     error = True

    # if not NAME_REGEX.match(request.POST['first_name']):
    #     messages.error(request,'first name field must  contain Alpha characters', extra_tags = 'fn_error')
    #     error = True

    # if not NAME_REGEX.match(request.POST['last_name']):
    #     messages.error(request,'Last name field must  contain Alpha characters', extra_tags = 'ln_error')
    #     error = True

    # if len(request.POST['last_name'])< 3:
    #     messages.error(request,'Last Name must be at least contain two characters', extra_tags = 'ln_error')
    #     error = True

    # if not EMAIL_REGEX.match(request.POST['email']):
    #     messages.error(request,'email format must matches the email patterns ', extra_tags = 'email_error')
    #     error = True

    # if check:
    #     messages.error(request,'Email has already been registered', extra_tags = 'email_error')
    #     error = True

    # if request.POST['password'] != request.POST['confirm_password']:
    #     messages.error(request,'Passwords do not match', extra_tags = 'pw_error')
    #     error = True

    # if len(request.POST['password']) < 8 :
    #     messages.error(request,'Password must be 8 or more characters long', extra_tags = 'pw_error')

    # if error == True:
    #     return redirect('/')

    # elif error == False:
    #     my_hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

    #     User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = my_hashed)

    #     messages.success(request, 'You have registered succesfully ,Thank you and welcome to this our web', extra_tags = 'registered')
        
    #     return redirect('/')

def login_validate(request):
    errors = User.objects.reg_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['user']=request.POST['email']

        redirect('/wall')

#     error = False
#     echeck = User.objects.filter(email=request.POST['email'])

#     if not EMAIL_REGEX.match(request.POST['email']):
#         messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
#         error = True
    
#     else:
#         if echeck:
#             if echeck[0].email == request.POST['email']:
#                 if echeck:
#                     request.session['login'] = True
#                     request.session['u_id'] = echeck[0].id
                    
#                 else:
#                     messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
#                     error = True
#             else:
#                 messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
#                 error = True
#         else:
#             messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
#             error = True

    

#     if error == True:
#         return redirect('/')
#     elif error == False:
#         return redirect('/home')


def wall(request):
    if request.session['login'] == True:
        user = User.objects.filter(email = request.session['user'])
        user_info = {
            'user':user[0]
        }
        return render(request, 'wall.html', user_info)

    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')



        
        



