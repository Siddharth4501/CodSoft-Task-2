from django.contrib import admin
from django.contrib.admin.sites import site



# Register your models here.
from travelbook.models import Booking,Flights,Contact
#class ContactAdmin(admin.ModelAdmin):
    #list_display=('username','email','phone','message')

#admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Flights)
admin.site.register(Contact)
