"""
URL configuration for POSTOFFICE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views 

urlpatterns = [
    #user
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('user_parcels/', views.user_parcels, name='user_parcels'),
    path('parcel_detail/<int:id>/', views.parcel_detail, name='parcel_detail'),  
    path('deleteuser/<int:did>',views.deleteuser,name='deleteuser'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('update_status/',views.update_status,name='update_status'),
    path('user_delivery_history/', views.user_delivery_history, name='user_delivery_history'),
    path('user_reschedule_history/', views.user_reschedule_history, name='user_reschedule_history'),
    path('delivered_parcels/', views.delivered_parcels, name='delivered_parcels'),
    path('rescheduled_parcels/', views.rescheduled_parcels, name='rescheduled_parcels'),
    path('returned_parcels/', views.returned_parcels, name='returned_parcels'),
    path('doorclosed_parcels/', views.doorclosed_parcels, name='doorclosed_parcels'),
    #feedback
    path('feedback_view/',views.feedback_view,name='feedback_view'),
    path('feedback_success/',views.feedback_success,name='feedback_success'),
    path('feedback_rate/',views.feedback_view,name='feedback_rate',),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('deletefeedback/',views.deletefeedback,name='deletefeedback'),
    path('deletefeedback/<int:id>',views.deletefeedback,name='deletefeedback'),
    #admin
    path('adminlogin2/',views.adminlogin2,name='adminlogin2'),
    path('adminhome2/',views.adminhome2,name='adminhome2'),
    path('adminlogin/',views.adminlogin,name='adminlogin'), 
    path('userlist/',views.userlist,name='userlist'),
    path('userlist2/',views.userlist2,name='userlist2'),
    path('adminhome/',views.adminhome,name='adminhome'),
    #stamp
    path('stamp/',views.createstamp,name='stamp'),
    path('stamplist/',views.stamplist,name='stamplist'),
    path('deletestamp/<int:id>',views.deletestamp,name='deletestamp'),
    path('editstamp/<int:id>/',views.edit_stamp, name='edit_stamp'),
    path('stamplist2/',views.stamplist2, name='stamplist2'),
    #postoffice
    path('postofficereg/',views.postofficereg,name='postofficereg'),
    path('postofficelist/',views.postofficelist,name='postofficelist'),
    path('postofficelist2/',views.postofficelist2,name='postofficelist2'),
    path('postofficelist3/',views.postofficelist3,name='postofficelist3'),
    path('deletepostoffice/<int:id>',views.deletepostoffice,name='deleteppostoffice'),
    path('editpostoffice/<int:id>/',views.edit_postoffice, name='editpostoffice'),
    #postman
    path('posthome/',views.posthome,name='posthome'),
    path('postmanreg/',views.postmanreg,name='postmanreg'),
    path('postmanlogin/',views.postmanlogin,name='postmanlogin'),
    path('postmanlist/',views.postmanlist,name='postmanlist'),
    path('postmanlist2/',views.postmanlist2,name='postmanlist2'),
    path('postmanlist3/',views.postmanlist3,name='postmanlist3'),
    path('deletepostman/<int:id>',views.deletepostman,name='deletepostman'),
    path('editpostman/<int:id>/',views.edit_postman, name='edit_postman'),
    path('postman_profile/',views.postman_profile,name='postman_profile'),
    path('postman_profile_delete/<int:pid>/',views.postman_profile_delete,name='postman_profile_delete'),
    path('postman_profile_edit/<int:pid>/',views.postman_profile_edit,name='postman_profile_edit'),
    path('update-status1/<int:id>/', views.update_status1, name='update_status1'),
   #parcel
    path('addparcel/',views.addparcel,name='addparcel'),
    path('parcellist/',views.parcellist,name='parcellist'),
    path('deleteparcel/<int:id>',views.deleteparcel,name='deleteparcel'),
    path('editparcel/<int:id>',views.edit_parcel,name='editparcel'),
    path('addparcel2/', views.addparcel2, name='addparcel2'),
    path('parcellist2/',views.parcellist2,name='parcellist2'),
    path('parcellist3/',views.parcellist3,name='parcellist3'),
    path('deleteparcel2/<int:id>',views.deleteparcel2,name='deleteparcel2'),
    path('editparcel2/<int:id>',views.edit_parcel2,name='editparcel2'),
    path('postmanparcel/',views.postmanparcel,name='postmanparcel'),
    path('deliveredstatus/<int:id>',views.delivered_status,name='deliveredstatus'),
    path('outdeliverystatus/<int:id>',views.outdelivery_status,name='outdeliverystatus'),
    path('poststatus/',views.poststatus,name='poststatus'),
    path('postmanparcel2/',views.postmanparcel2,name='postmanparcel2'),
    path('deliveredstatus/<int:id>',views.delivered_status,name='deliveredstatus'),
    path('reschedule/<int:id>',views.reschedule,name='reschedule'),
    path('view_reschedule_details/<int:id>/',views.rescheduled_details,name='reschedule_details'),
    path('approve_reschedule/<int:id>/', views.approve_reschedule, name='approve_reschedule'),
    path('reject_reschedule/<int:id>/', views.reject_reschedule, name='reject_reschedule'),
    path('initiate_payment/<int:reschedule_id>/', views.initiate_payment, name='initiate_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    #fpw
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
]
