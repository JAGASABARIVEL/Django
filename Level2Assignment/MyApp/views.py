from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse

from MyApp.forms import (ReportSearchForm, RegisterLorryForm,
                        CreateBookingForm, UserForm,
                        UserProfileForm, CreateStagingForm,
                        CompleteBookingForm, SearchLorryForm,
                        RegisterClientForm, RegisterDriverForm,
                        VehicleTypeForm, PlacesForm,
                        LoadTypeForm,)

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

def home(request):
    global_sync = {"content_output":""}
    if request.user.is_authenticated:
        UserId = request.user.id
        UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
        if UserType == 'LO':
            global_sync = {"content_output":"O"}
        elif UserType == 'MA':
            global_sync = {"content_output":"M"}
        elif UserType == 'AO':
            global_sync = {"content_output":"A"}
        elif UserType == 'NU':
            global_sync = {"content_output":"U"}
        else:
            global_sync = {"content_output":""}
    return render(request, "home.html", context=global_sync)

@login_required
def register_lorry(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType != "LO":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
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
                messages.success(request, "Your lorry has been registered successfully!")
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, "register_lorry_error.html", {})
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def register_places_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = PlacesForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place = form.cleaned_data['place']
            instance.save()
            messages.success(request, "Place %s has been registered successfully!" %(instance.place))
            return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def register_vehicle_type_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = VehicleTypeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vehicletype = form.cleaned_data['vehicletype']
            instance.save()
            messages.success(request, "Vehicle type %s has been registered successfully!" %(instance.vehicletype))
            return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})


@login_required
def register_driver_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = RegisterDriverForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = form.cleaned_data["name"]
            instance.phone_number = form.cleaned_data["phone_number"]
            instance.address = form.cleaned_data["address"]
            instance.referedby = request.user
            instance.save()
            messages.success(request, "Driver got registered successfully.")
            return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def register_client_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = RegisterClientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = form.cleaned_data["name"]
            instance.phone_number = form.cleaned_data["phone_number"]
            instance.address = form.cleaned_data["address"]
            instance.referedby = request.user
            instance.save()
            messages.success(request, "Client got registered successfully.")
            return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def register_loadtype_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = LoadTypeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.loadtype = form.cleaned_data["loadtype"]
            instance.save()
            messages.success(request, "Load Type %s got registered successfully." %(instance.loadtype))
            return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def create_staging(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = CreateStagingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
                instance = form.save(commit=False)
                instance.staginguser = request.user
                instance.lorryid = form.cleaned_data["lorryid"]
                instance.driverid = form.cleaned_data["driverid"]
                instance.startdate = form.cleaned_data["startdate"]
                instance.starttime = form.cleaned_data["starttime"]
                instance.from_place = form.cleaned_data["from_place"]
                instance.to_place = form.cleaned_data["to_place"]
                instance.estimated_amount = form.cleaned_data["estimated_amount"]
                instance.save()
                messages.success(request, "Staging of the lorry %s has been successfull." % (instance.lorryid))
                return HttpResponseRedirect(reverse('home'))
    return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})

@login_required
def search_lorry_for_booking(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
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
    return render(request, "common_form_display.html", {"form":form, "content_output" : global_sync["content_output"]})

@login_required
def create_user_booking(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        id = request.POST.get('_id')
        request.session['booking_lorry_id'] = id
        return HttpResponseRedirect(reverse('my_booking_process'))
    return render(request, "common_form_display.html", {"content_output" : global_sync["content_output"]})


@login_required
def my_booking_process_view(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    booking_lorry_id = request.session.get('booking_lorry_id', -1)
    if booking_lorry_id == -1:
        messages.success(request, "You can not book directly without selecting the lorry.")
        return HttpResponseRedirect(reverse('home'))
    booking_detail = Booking.objects.get(id=booking_lorry_id)
    form = CreateBookingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            booking_detail.driverid = form.cleaned_data['driverid']
            booking_detail.client_name = form.cleaned_data['client_name']
            booking_detail.load_type = form.cleaned_data['load_type']
            booking_detail.bookinguser = request.user
            booking_detail.state = "BOOKED"
            booking_detail.save()
            request.session['booking_lorry_id'] = -1
            messages.success(request, "Booking has been completed successfully.")
            return HttpResponseRedirect(reverse('my_book'))
        return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})
    return render(request, "common_form_display.html", {"form" : form, "headercontent":"CONFIRM BOOKING", "content_output" : global_sync["content_output"]})

@login_required
def complete_booking_option(request):
    global complete_booking_lorry_id
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    book_history = Booking.objects.filter(state="BOOKED")
    return render(request, "booking_complete.html", {"book_history":book_history, "content_output" : global_sync["content_output"]})

@login_required
def complete_booking_form(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    lorry = ''
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        complete_booking_lorry_id = request.POST.get('_id')
        request.session['complete_booking_lorry_id'] = complete_booking_lorry_id
        return HttpResponseRedirect(reverse('my_complete_process'))
    return render(request, "home.html", {"content_output" : global_sync["content_output"]})

@login_required
def complete_booking_form_process(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    complete_booking_lorry_id = request.session.get('complete_booking_lorry_id', -1)
    if complete_booking_lorry_id == -1:
        messages.success(request, "You can not complete the booking directly without selecting the booking.")
        return HttpResponseRedirect(reverse('home'))
    booking_detail = Booking.objects.get(id=complete_booking_lorry_id)
    form = CompleteBookingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            booking_detail.driverid = form.cleaned_data['driverid']
            booking_detail.endkm = form.cleaned_data['endkm']
            booking_detail.amount = form.cleaned_data['amount']
            booking_detail.dieselcost = form.cleaned_data['dieselcost']
            booking_detail.tollcost = form.cleaned_data['tollcost']
            booking_detail.policecost = form.cleaned_data['policecost']
            booking_detail.othercost = form.cleaned_data['othercost']
            booking_detail.state = "COMPLETED"
            booking_detail.completedby = request.user
            booking_detail.save()
            request.session['complete_booking_lorry_id'] = -1
            messages.success(request, "Booking has been completed successfully.")
            return HttpResponseRedirect(reverse('home'))
        return render(request, "common_form_display.html", {"form" : form, "content_output" : global_sync["content_output"]})
    return render(request, "common_form_display.html", {"headercontent":"CONFIRM COMPLETE BOOKING","form" : form, "content_output" : global_sync["content_output"]})

@login_required
def cancel_bookings(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        id = request.POST.get('_id')
        lorry = Booking.objects.get(id=id)
        if lorry.state == "BOOKED" or lorry.state == "ONHOLD":
            lorry.bookinguser = request.user
            lorry.state = "CANCELLED"
            lorry.cancelledby = request.user
            lorry.save()
    return HttpResponseRedirect(reverse('my_book'))

#########################################################################
#
#                        REPORTS CODE
#
#########################################################################
@login_required
def my_bookings(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    _state = ["BOOKED", "COMPLETED", "CANCELLED"]
    if UserType != "NU":
        book_history = Booking.objects.filter(state__in=_state)
        return render(request, "booking_history.html", {"book_history": book_history, "content_output" : global_sync["content_output"]})
    else:
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))

@login_required
def report_search(request):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    form = ReportSearchForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            lorryid = form.cleaned_data["lorryid"]
            from_date = form.cleaned_data["from_date"]
            fromtime = form.cleaned_data["fromtime"]
            todate = form.cleaned_data["todate"] + timedelta(days=1)
            totime = form.cleaned_data["totime"]
            content = {"filter":{"lorryid":lorryid,
                                "from_date":from_date,
                                "todate":todate}}
            return get_report(request, content)
    return render(request, "report_search.html", {"form" : form, "content_output" : global_sync["content_output"]})


@login_required
def get_report(request, contents=''):
    print("contents : ", len(contents))
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    if UserType == 'MA' or UserType == 'AO':
        if len(contents) == 0:
            lorry_history = Booking.objects.all()
            return render(request, "reports.html", {'lorry_history':lorry_history, "content_output" : global_sync["content_output"]})
        else:
            lorry_id = contents['filter']['lorryid']
            from_date = contents['filter']['from_date']
            to_date = contents['filter']['todate']
            lorry_history = Booking.objects.filter(lorryid=lorry_id, bookingdate__range=[from_date, to_date])
            return render(request, "reports.html", {"lorry_history":lorry_history, "content_output" : global_sync["content_output"]})
    elif UserType == 'LO':
        lorry_numbers = RegisterLorry.objects.filter(user=request.user).values('lorry_number')
        shaved_lorry_numbers = []
        for lo_number in lorry_numbers:
            shaved_lorry_numbers.append(lo_number["lorry_number"])
        if len(contents) == 0:
            lorry_history = Booking.objects.filter(lorryid__in=shaved_lorry_numbers)
            return render(request, "reports.html", {'lorry_history':lorry_history, "content_output" : global_sync["content_output"]})
        else:
            lorry_id = contents['filter']['lorryid']
            from_date = contents['filter']['from_date']
            to_date = contents['filter']['todate']
            if lorry_id in shaved_lorry_numbers:
                lorry_history = Booking.objects.filter(lorryid=lorry_id, bookingdate__range=[from_date, to_date])
                return render(request, "reports.html", {"lorry_history":lorry_history, "content_output" : global_sync["content_output"]})
            else:
                messages.success(request, "You need to be an manager or owner of the lorry to view reports other than your lorry.")
                return HttpResponseRedirect(reverse('home'))

@login_required
def view_report_owner(request, contents=False):
    global_sync = {"content_output":""}
    UserId = request.user.id
    UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
    if UserType == 'LO':
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
    lorry_numbers = RegisterLorry.objects.filter(user=request.user).values('lorry_number')
    shaved_lorry_numbers = []
    for lo_number in lorry_numbers:
        shaved_lorry_numbers.append(lo_number["lorry_number"])
    lorry_history = Booking.objects.filter(lorryid__in=shaved_lorry_numbers)
    return render(request, "reports.html", locals())

#########################################################################
#
#                    AUTHENTICATION CODE PART
#
#########################################################################

def register_user(request):
    registered = False
    global_sync = {"content_output":""}
    if request.user.is_authenticated:
        registered = True
        UserId = request.user.id
        UserType = (UserProfile.objects.values('user_type').filter(user=UserId))[0]['user_type']
        if UserType == 'LO':
            global_sync = {"content_output":"O"}
        elif UserType == 'MA':
            global_sync = {"content_output":"M"}
        elif UserType == 'AO':
            global_sync = {"content_output":"A"}
        elif UserType == 'NU':
            global_sync = {"content_output":"U"}
        else:
            global_sync = {"content_output":""}
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
        global_sync = {"content_output":"O"}
    elif UserType == 'MA':
        global_sync = {"content_output":"M"}
    elif UserType == 'AO':
        global_sync = {"content_output":"A"}
    elif UserType == 'NU':
        global_sync = {"content_output":"U"}
    else:
        global_sync = {"content_output":""}
    if UserType == "NU":
        messages.success(request, "You are not an authorized user.")
        return HttpResponseRedirect(reverse('home'))
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
