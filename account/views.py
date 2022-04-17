from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as loginFunc, logout as logoutFunc
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from .models import Profile
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url="login")
def home(request):
    context = {}
    user = Profile.objects.get(username=request.user.username)
    context["fname"] = user.first_name
    context["lname"] = user.last_name
    context["username"] = user.username
    context["email"] = user.email
    context["image"] = user.image
    context["utype"] = request.user.groups.all()[0]
    return render(request,"index.html",context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        context = {"form":form}
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                loginFunc(request,user)
                return redirect("home")
        else: 
            return render(request,"login.html",context)
    else:
        form = AuthenticationForm()
        context = {"form":form}
        return render(request,"login.html",context)

def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST, request.FILES)
        context = {"form":form}
        if form.is_valid():
            add_data = Profile()
            add_data.username = form.cleaned_data.get("username")
            add_data.first_name = form.cleaned_data.get("first_name")
            add_data.last_name = form.cleaned_data.get("last_name")
            add_data.email = form.cleaned_data.get("email")
            add_data.image = form.cleaned_data.get("image")
            add_data.save()
            user = form.save()
            user_group = Group.objects.get_or_create(name=request.POST.get("user")) 
            user.groups.add(user_group[0])
            if user is not None:
                return redirect("login")
        else:
            return render(request,"signup.html",context)
    else:
        form = UserCreateForm()
        context = {"form":form}
        return render(request,"signup.html",context)

@login_required(login_url="login")
def logout(request):
    logoutFunc(request)
    return redirect("login")