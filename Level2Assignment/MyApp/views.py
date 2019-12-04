from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from MyApp.forms import (ReportSearchForm, RegisterLorryForm,
                        CreateBookingForm, UserForm,
                        UserProfileForm, CreateStagingForm,
                        CompleteBookingForm, SearchLorryForm,
                        RegisterDriverForm,)

from MyApp.models import RegisterLorry, Booking, UserProfile, SearchLorry
###############################
# IMPORTS NECESSARY FOR LOGIN #
###############################
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
context = {"create_user_booking":{"error":""}}

def home(request):
    global_sync = {"content_output":""}
    if request.user.is_authenticated:
        UserId = request.user.id
        UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
        if UserType == 'LO':
            global_sync = {"content_output":"XXXX"}
    return render(request, "home.html", context=global_sync)

@login_required
def report_search(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = ReportSearchForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            lorryid = form.cleaned_data["lorryid"]
            from_date = form.cleaned_data["from_date"]
            fromtime = form.cleaned_data["fromtime"]
            todate = form.cleaned_data["todate"]
            totime = form.cleaned_data["totime"]
        content = {"content":{"lorryid":lorryid, "from_date":from_date,
                             "fromtime":fromtime, "todate":todate,
                             "totime":totime}}
        return view_report_owner(request)
    return render(request, "report_search.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def register_lorry(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = RegisterLorryForm(request.POST)
    if request.method == "POST":
        form = RegisterLorryForm(request.POST)
        if form.is_valid():
            if UserType == 'LO':
                instance = form.save(commit=False)
                instance.user = request.user
                instance.vehicle_type = form.cleaned_data['vehicle_type']
                instance.lorry_number = form.cleaned_data['lorry_number']
                instance.year_model = form.cleaned_data['year_model']
                instance.save()
                return HttpResponseRedirect(reverse('search_lorry'))
            else:
                return render(request, "register_lorry_error.html", {})
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def create_bookings(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    if request.method == "POST":
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lorryid = form.cleaned_data["lorryid"]
            instance.driverid = form.cleaned_data["driverid"]
            instance.bookingdate = form.cleaned_data["bookingdate"]
            instance.tripdate = form.cleaned_data["tripdate"]
            instance.amount = form.cleaned_data["amount"]
            instance.save()
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def search_lorry_for_booking(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = SearchLorryForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.loading_area = form.cleaned_data["loading_area"]
        instance.unloading_area = form.cleaned_data["unloading_area"]
        instance.date_to_be_looked = form.cleaned_data["date_to_be_looked"]
        instance.save()
        available_lorry = Booking.objects.filter(from_place=instance.loading_area,
                               to_place=instance.unloading_area,
                               startdate= instance.date_to_be_looked,
                               state__in=["NEW", "CANCELLED"])
        return render(request, 'available_lorry.html', locals())
    return render(request, "common_form_display.html", {"form":form, "context":context["create_user_booking"], "content_output" : global_sync["content_output"]})

@login_required
def create_staging(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = CreateStagingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            if UserType == 'LO':
                instance = form.save(commit=False)
                instance.lorryid = form.cleaned_data["lorryid"]
                instance.driverid = form.cleaned_data["driverid"]
                instance.startdate = form.cleaned_data["startdate"]
                instance.starttime = form.cleaned_data["starttime"]
                instance.from_place = form.cleaned_data["from_place"]
                instance.to_place = form.cleaned_data["to_place"]
                instance.estimated_amount = form.cleaned_data["estimated_amount"]
                instance.save()
            else:
                return render(request, "register_lorry_error.html", {})
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def create_user_booking(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    if request.method == 'POST':
        id = request.POST.get('_id')
        lorry = Booking.objects.get(id=id)
        if lorry.state != "BOOKED" or lorry.state != "ONHOLD":
            lorry.bookinguser = request.user
            lorry.state = "BOOKED"
            lorry.save()
            return HttpResponseRedirect(reverse('my_book'))
        else:
            context["create_user_booking"]["error"] = "Lorry %s has been already been booked. Please try to book anyother lorry." % (lorry.lorryid)
            return HttpResponseRedirect(reverse('search_lorry'))
    return render(request, "common_form_display.html", {"content_output" : global_sync["content_output"]})

@login_required
def cancel_bookings(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    if request.method == 'POST':
        id = request.POST.get('_id')
        lorry = Booking.objects.get(id=id)
        if lorry.state == "BOOKED" or lorry.state == "ONHOLD":
            lorry.bookinguser = request.user
            lorry.state = "CANCELLED"
            lorry.save()
    return HttpResponseRedirect(reverse('my_book'))

@login_required
def my_bookings(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    book_history = Booking.objects.filter(bookinguser=request.user)
    return render(request, "booking_history.html", locals())

@login_required
def complete_booking_option(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    book_history = Booking.objects.filter(bookinguser=request.user)
    return render(request, "booking_complete.html", locals())

@login_required
def register_driver_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = RegisterDriverForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if UserType == 'LO':
                instance = form.save(commit=False)
                instance.name = form.cleaned_data["name"]
                instance.phone_number = form.cleaned_data["phone_number"]
                instance.address = form.cleaned_data["address"]
                instance.save()
                messages.success(request, "Driver has been registered successfully.")
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, "register_lorry_error.html", {"content_output" : global_sync["content_output"]})
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def complete_booking_form(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    if request.method == 'POST':
        complete_booking_lorry_id = request.POST.get('_id')
        return complete_booking_form_process(request, complete_booking_lorry_id)
    return render(request, "home.html", {"content_output" : global_sync["content_output"]})

@login_required
def complete_booking_form_process(request, complete_booking_lorry_id):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    form = CompleteBookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            lorry = Booking.objects.get(id=complete_booking_lorry_id)
            lorry.driverid = form.cleaned_data["driverid"]
            lorry.endkm = form.cleaned_data["endkm"]
            lorry.amount = form.cleaned_data["amount"]
            lorry.dieselcost = form.cleaned_data["dieselcost"]
            lorry.tollcost = form.cleaned_data["tollcost"]
            lorry.policecost = form.cleaned_data["policecost"]
            lorry.othercost = form.cleaned_data["othercost"]
            lorry.save()
            return render(request, "home.html", {"content_output" : global_sync["content_output"]})
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def view_report_owner(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    lorry_numbers = RegisterLorry.objects.filter(user=request.user).values('lorry_number')
    print(lorry_numbers)
    shaved_lorry_numbers = []
    for lo_number in lorry_numbers:
        shaved_lorry_numbers.append(lo_number["lorry_number"])
    lorry_history = Booking.objects.filter(lorryid__in=shaved_lorry_numbers)
    return render(request, "reports.html", locals())

def register_user(request):
    registered = False
    if request.user.is_authenticated:
        registered = True
        return render(request, "register.html", {"already_registered" : True, "content_output" : global_sync["content_output"]})

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_instance = user_form.save(commit=False)
            profile_instance = profile_form.save(commit=False)
            user_instance.set_password(profile_instance.password)
            user_instance.save()
            profile_instance.user = user_instance
            if 'profile_pic' in request.FILES:
                profile_instance.profile_pic = request.FILES['profile_pic']
            profile_instance.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
    return render(request, "register.html", {'user_form' : user_form,
                                              'profile_form' : profile_form,
                                              'registered' : registered,
                                              })

@login_required
def view_option(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"XXXX"}
    return render(request, "option.html", {"content_output" : global_sync["content_output"]})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('_username')
        password = request.POST.get('_password')
        print("Username : {}\nPassword : {}".format(username, password))
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, "login_error.html", {})
        else:
            print("Unatorized access by the user : {} at {}".format(username, datetime.now()))
            return render(request, "login_error.html", {})
    else:
        return render(request, "login.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
