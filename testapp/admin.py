from django.contrib import admin
from testapp.models import Rental
from testapp.models import User
from testapp.models import Hire

# Register your models here.
class RentalAdmin(admin.ModelAdmin):
    list_display=['name','MobileNumber','Address','pincode','image','rentalamount','tractormodel']

admin.site.register(Rental,RentalAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=['name','numofhours','datetime','address','pincode']

admin.site.register(User,UserAdmin)

class HireAdmin(admin.ModelAdmin):
    list_display=['name','numofdays','datetime','address','pincode']

admin.site.register(Hire,HireAdmin)