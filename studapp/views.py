from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# from studapp.models import Registration
from studapp.models import Accommodation
from studapp.models import Enquire
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home Page")


def home(request):
    return render(request, 'index.html')


def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if len(username) > 10:
            messages.warning(request, "Username must be under 10 characters")
            return redirect(reverse('studapp'))

        if not username.isalnum():
            messages.warning(
                request, "Username should only contain letters and numbers")
            return redirect(reverse('studapp'))

        if password != password2:
            messages.error(request, "Password do not match")
            return redirect(reverse('studapp'))
    #    / myuser = Registration(name=name, email=email, password=password,
            # mobile_no=mobile_no, address=address, date=datetime.today())
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'Your Account has been successfully created !')
        return redirect(reverse('studapp'))
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == "POST":
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        user = authenticate(username=login_username, password=login_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In !")
            return redirect(reverse('studapp'))
        else:
            messages.error(request, "Invalid Credentials, Please try again !")
            return redirect(reverse('studapp'))


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out !")
    return redirect(reverse('studapp'))


def handleaccommodation(request):
    allAccommodation = Accommodation.objects.all()
    context = {'accommodations': allAccommodation}
    return render(request, 'accommodation.html', context)


def search(request):
    query = request.GET['query']
    allAccommodation = Accommodation.objects.filter(a_address__icontains=query)
    context = {'allaccommodations': allAccommodation}
    return render(request, 'search.html', context)


def enquire(request):
    if request.method == "POST":
        e_user_id = request.user.id
        e_phone = request.POST['e_phone']
        e_query = request.POST['e_query']

        myenquire = Enquire(e_user_id_id=e_user_id,e_phone=e_phone,
                            e_query=e_query, e_date=datetime.today())
        myenquire.save()
        messages.success(
            request, 'Your Enquiry successfully Sent !')
        return redirect(reverse('studapp'))
