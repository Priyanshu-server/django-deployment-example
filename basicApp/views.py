# basic imports
from django.shortcuts import render, reverse
from basicApp.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponseRedirect, HttpResponse

# Login Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# Logout function doesn't seems to work ...

def index(request):
    return render(request, "index.html")


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html', {'user_form': user_form,
                                             'profile_form': profile_form,
                                             'registered': registered})


def contact(request):
    return render(request, "contact.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("basicApp:home"))

            else:
                return HttpResponse("Account not activated !")
        else:
            print('Someone tried to login and failed !')
            print("Username : {} and Password {}".format(username, password))
            return HttpResponse("Invalid Login Details")
    else:
        return render(request, "login.html")


@login_required
def user_logout(request):
    logout(request)
    # if request.session:
    #     request.session.flush()
    return HttpResponseRedirect(reverse("basicApp:home"))


@login_required
def special(request):
    return HttpResponse("<h1>Logged In !</h1>")
