import json
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm
from .forms import UserLoginAdminForm


def home(request):
    return render(request, 'users/home.html')


@csrf_exempt
def isadmin(request):
    if request.method == 'POST':
        form = UserLoginAdminForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            if user is not None:
                if user.is_superuser and user.is_staff:
                    user = get_user_model()
                    users = user.objects.all()
                    return render(request, 'users/userdetails.html', context={'users': users})
                else:
                    form = UserLoginAdminForm()
                    messages.error(request, "Possess Admin/SuperUser privileges!!!!")
                    return render(request, 'users/adminlogin.html', context={'form': form})

            else:
                form = UserLoginAdminForm()
                messages.error(request, "Login Failed , Ensure You are a registered User!!!!!!")
                return render(request, 'users/adminlogin.html', context={'form': form})

    elif request.method == 'DELETE':
        deleteuser(request.GET.get("deleteId"))
        user = get_user_model()
        users = user.objects.all()
        return render(request, 'users/userdetails.html', context={'users': users})

    else:
        form = UserLoginAdminForm()
        return render(request, 'users/adminlogin.html', context={'form': form})


def deleteuser(userid):
    obj = get_object_or_404(get_user_model(), id=userid)
    obj.delete()


def updateuser(request):
    if request.method == 'POST':
        updateduser = get_user_model().objects.get(id=request.POST['userId'])
        updateduser.username = request.POST['userName']
        updateduser.first_name = request.POST['firstName']
        updateduser.last_name = request.POST['lastName']
        updateduser.email = request.POST['emailId']
        updateduser.save()
        return render(request, 'users/userdetails.html', context={'users': get_user_model().objects.all()})
    else:
        form = UserLoginAdminForm()
        return render(request, 'users/adminlogin.html', context={'form': form})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)