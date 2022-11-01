
from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, Customerform,Topicform
from .models import Customer, Topic


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
   
    if request.method == "POST":
        form = Topicform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('office')
            except:
                pass
    Topics = Topic.objects.all()
    return render(request, "Office\index.html", {'Topic': Topics})
    


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


def emp(request):
    if request.method == "POST":
        form = Customerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('showme')
            except:
                pass
    else:
        form = Customerform()
    return render(request, 'Staff\index.html', {'form': form})


def showme(request):
    Customers = Customer.objects.all()
    return render(request, "Staff\show.html", {'Customer': Customers})


def edit(request, id):
    Customers = Customer.objects.get(id=id)    
    return render(request, 'Staff\edit.html', {'Customer': Customers})


def update(request, id):
    Customers = Customer.objects.get(id=id)
    print(Customers)
    form = Customerform(request.POST, instance=Customers)
    if form.is_valid():
        form.save()
        return redirect("showme")
    return render(request, 'Staff\edit.html', {'Customer': Customers})


def destroy(request, id):
    Customers = Customer.objects.get(id=id)
    Customers.delete()
    return redirect("showme")



# report mate no code
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import  A4
from reportlab.lib.units import inch


def Brochure(request):    
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
       
    # Close the PDF object cleanly, and we're done.
    p.translate(inch,inch)
    # define a large font
    p.setFont("Helvetica", 14)
    # choose some colors
   

    my_image = ImageReader('Static/Images/favicon.png')
    p.drawImage(my_image, 10, 600, mask='auto')
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')  
    p.drawString( 0,700,ts )
    p.drawString(100, 100,"Hello World")
    p.setTitle('Brochure')
    p.showPage() 
    p.save() 

    # Show the result to the user    
 
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)   
    return FileResponse(buffer, as_attachment=True, filename="Brochure.pdf")

    
