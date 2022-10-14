from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")


def Service(request):
    return render(request, "Service.html")


def Area(request):
    return render(request, "Area.html")


def u_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("office")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid username or password.")
            return render(request, 'Client/Login.html')

    return render(request, 'Client/Login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


def office(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, "Office\index.html")


def client(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, "Client\index.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(
            username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.info(
            request, "Account created successfully please login again")

        return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
