from django.urls import path
from . import views


urlpatterns = [
    
    path('home/',views.home,name="home"),
    path('signin/',views.signin,name="signin"),
    path('login/',views.handleLogin,name="login"),
    path('about/',views.about),
    path('payment/',views.payment,name="pay"),
    path('user/',views.user,name="user"),
    path('contact/',views.contact1,name="contact"),
    path('signup/',views.handleSignup,name="signup"),
    path('bookingsearchresult/',views.bkr,name="bkr"),
    path('thanks/',views.thanks,name="thanks"),
    path('bookingreceipt/',views.bookingreceipt,name="bookreceipt"),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('logout/',views.logOUT,name="logout"),

]