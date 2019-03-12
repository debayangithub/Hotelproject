from django.shortcuts import render
from django.conf.urls import url
from superIndex.forms import Customer_Form,User_Form
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    return render(request,'superIndex/homepage.html')

def standard_room(request):
    return render(request,'superIndex/standard_room.html')

def luxury_room(request):
    return render(request,'superIndex/luxury_room.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    register = False

    if request.method == "POST":
        userform = User_Form(data=request.POST)
        customerform = Customer_Form(data=request.POST)

        if userform.is_valid() and customerform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            customer = customerform.save(commit=False)
            customer.user = user
            customer.save()

            register = True
            return index(request)
        else:
            print(User_Form.errors,Customer_Form.errors)


    else:
        userform = User_Form()
        customerform = Customer_Form()
        return render(request,'superIndex/registration.html',
                                {'userform':userform,
                                 'customerform':customerform,
                                 'register':register
                                })

def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active!")
        else:
            print("Someone Tried to login but failed")
            print("Username: {} and Password : {}.format(username,password)")
            return HttpResponse('Invalid login details provided')
    else:
        return render(request,'superIndex/login.html',{})
