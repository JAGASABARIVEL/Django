from django import forms

###################################
# FOR CRISPY FILTERS FUCTIONALITY #
###################################
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field
from crispy_forms.bootstrap import PrependedText

##################################
# FOR SHOWCASING MODELS IN FORMS #
##################################
from MyApp.models import RegisterLorry, Booking, SearchLorry, RegisterDriver

###############################################
# FOR BOOTSTRAP'S DATE AND TIME PICKER WIDGET #
###############################################
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

####################
# FOR REGISTRATION #
####################
from django.contrib.auth.models import User
from MyApp.models import UserProfile

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReportSearchForm(forms.Form):
    lorryid = forms.IntegerField()
    from_date = forms.DateField(widget=DatePickerInput(attrs={'class': 'datepicker'}))
    fromtime = forms.TimeField(widget=TimePickerInput())
    todate = forms.DateField(widget=DatePickerInput(attrs={'class': 'datepicker'}))
    totime = forms.TimeField(widget=TimePickerInput())

    def __init__(self, *args, **kwargs):
        super(ReportSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class RegisterLorryForm(forms.ModelForm):
    class Meta:
        model=RegisterLorry
        exclude = ['user']
        forms.Form.helper = FormHelper()

class CreateStagingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('lorryid', 'driverid', 'startdate', 'starttime',
                 'from_place', 'to_place', 'estimated_amount',)
        widgets = {
            'startdate': DatePickerInput(attrs={'class': 'datepicker'}),
            'starttime': TimePickerInput()
        }
        forms.Form.helper = FormHelper()

class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = RegisterDriver
        fields = ('name', 'phone_number', 'address', 'referedby')
        forms.Form.helper = FormHelper()

class SearchLorryForm(forms.ModelForm):
    class Meta:
        model = SearchLorry
        fields = ('loading_area', 'unloading_area', 'date_to_be_looked')
        widgets = {
            'date_to_be_looked': DatePickerInput(attrs={'class': 'datepicker'})
        }
        forms.Form.helper = FormHelper()

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('lorryid', 'driverid', 'bookingdate', 'amount')
        widgets = {
            'tripdate': DatePickerInput(attrs={'class': 'datepicker'})
        }
        forms.Form.helper = FormHelper()

class CompleteBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('driverid', 'endkm', 'amount', 'dieselcost', 'tollcost', 'policecost', 'othercost')
        widgets = {
            'tripdate': DatePickerInput(attrs={'class': 'datepicker'})
        }
        forms.Form.helper = FormHelper()

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fileds = ('username',)
        exclude = ('groups', 'user_permissions', 'is_staff', 'is_active',
                    'is_superuser', 'date_joined', 'last_login',
                    'first_name', 'last_name', 'email', 'password',)
        forms.Form.helper = FormHelper()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('password', 'confirm_password', 'phone', 'confirm_phone', 'user_blog', 'user_image')
        forms.Form.helper = FormHelper()

    def clean(self):
        super(UserProfileForm, self).clean()
        phone = self.cleaned_data['phone']
        confirm_phone = self.cleaned_data['confirm_phone']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if len(password) == 0:
            self._errors['password'] = self.error_class(
            ['Password can not be empty.']
            )
        if len(confirm_password) == 0:
            self._errors['confirm_password'] = self.error_class(
            ['Confirm Password can not be empty.']
            )

        if len(password) == 0:
            self._errors['phone'] = self.error_class(
            ['Phone can not be empty.']
            )
        if len(confirm_password) == 0:
            self._errors['confirm_phone'] = self.error_class(
            ['Confirm Phone can not be empty.']
            )

        if password != confirm_password:
            self._errors['confirm_password'] = self.error_class(
            ['Both password number and confirm password number should be matching.']
            )
        if phone != confirm_phone:
            self._errors['confirm_phone'] = self.error_class(
            ['Both phone number and confirm phone number should be matching.']
            )
            print("I am here si")
        return self.cleaned_data
