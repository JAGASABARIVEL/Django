from django.urls import include, path
from MyApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.report_search, name="reportSearch"),
    path('mySales/', views.view_report_owner, name="my_sale"),
    path('registerLorry/', views.register_lorry, name="registerLorry"),
    path('createStaging/', views.create_staging, name="create_staging"),
    path('searchLorry/', views.search_lorry_for_booking, name="search_lorry"),
    path('registerUser/', views.register_user, name="registerUser"),
    path('userLogin/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('option/', views.view_option, name='option'),
    path('createUserBooking/', views.create_user_booking, name="create_user_booking"),
    path('myBookings/', views.my_bookings, name="my_book"),
    path('cancelBookings/', views.cancel_bookings, name="my_cancel"),
    path('completeBookingsOption/', views.complete_booking_option, name="my_complete_option"),
    path('completeBookings/', views.complete_booking_form, name="my_complete"),
    path('completeBookingsProcess/', views.complete_booking_form_process, name="my_complete_process"),
    path('registerDriver/', views.register_driver_view, name="register_driver_view"),
    path('registerClient/', views.register_client_view, name="register_client"),
    path('bookingProcess/', views.my_booking_process_view, name="my_booking_process"),
    path('registerPlace/', views.register_places_view, name="register_places"),
    path('registerVehicle/', views.register_vehicle_type_view, name="register_vehicle_type"),
    path('registerLoadType/', views.register_loadtype_view, name="register_loadtype"),
]
