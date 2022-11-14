from django.shortcuts import render
from auth_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'auth_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You're logged in, nice")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileInfoForm()

    return render(request, 'auth_app/registration.html', {'user_form':user_form, 'profile_form':user_profile, 'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details supplied")
    else:
        return render(request, 'auth_app/login.html')