from django.shortcuts import render

# from django.views.generic import CreateView, ListView
from testapp.forms import RentalForm
from testapp.forms import UserForm
from testapp.forms import HireForm
#from testapp.models import User
#from testapp.models import Rental
#from testapp.models import Hire

# Create your views here.
# class RentalListView(ListView):
#    model = Rental
#
# class UserListView(ListView):
#    model = User
#
# class HireListView(ListView):
#    model = Hire


def front_view(request):
    return render(request, "testapp/front.html")


def about_view(request):
    return render(request, "testapp/about.html")

def contact_view(request):
    return render(request, "testapp/contact.html")


def utility_view(request):
    return render(request, "testapp/utility.html")


def compact_view(request):
    return render(request, "testapp/compact.html")


def rowcrop_view(request):
    return render(request, "testapp/rowcrop.html")


def industrial_view(request):
    return render(request, "testapp/industrial.html")


def twowheel_view(request):
    return render(request, "testapp/twowheel.html")


def backhoe_view(request):
    return render(request, "testapp/backhoe.html")


def rental_view(request):
    form = RentalForm()
    submitted = False
    if request.method == "POST":
        form = RentalForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
    return render(
        request, "testapp/rentalform.html", {"form": form, "submitted": submitted}
    )


def user_view(request):
    form = UserForm()
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    return render(
        request, "testapp/userform.html", {"form": form, "submitted": submitted}
    )


def hire_view(request):
    form = HireForm()
    submitted = False
    if request.method == "POST":
        form = HireForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    return render(
        request, "testapp/hireform.html", {"form": form, "submitted": submitted}
    )


# def rental_view(request):
#    submitted=False
#    form = RentalForm()
#    if request.method == 'POST':
#        form = RentalForm(request.POST)
#        if form.is_valid():
#            form.save()
#            submitted = True
#            return render(request , "testapp/rentalform.html" , {"form":form , "message":"Submitted Succesfully"})
#        else:
#            return render(request , "testapp/rentalform.html" , {"form":form , "message":"Record Submitted Successfully"})
#    return render(request,'testapp/rentalform.html',{'form':form, 'submitted':submitted})
# def user_view(request):
#    submitted=False
#    form = UserForm()
#    if request.method == 'POST':
#        form = UserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            submitted = True
#            return render(request , "testapp/userform.html" , {"form":form , "message":"Submitted Succesfully"})
#        else:
#            return render(request , "testapp/userform.html" , {"form":form , "message":"Record Submitted Successfully"})
#    return render(request,'testapp/userform.html',{'form':form, 'submitted':submitted})
#
# def hire_view(request):
#    submitted=False
#    form = HireForm()
#    if request.method == 'POST':
#        form = HireForm(request.POST)
#        if form.is_valid():
#            form.save()
#            submitted = True
#            return render(request , "testapp/hireform.html" , {"form":form , "message":"Submitted Succesfully"})
#        else:
#            return render(request , "testapp/hireform.html" , {"form":form , "message":"Record Submitted Successfully"})
#    return render(request,'testapp/hireform.html',{'form':form, 'submitted':submitted})
#
#
# def User_view(request):
#    submitted=False
#    form = UserForm()
#    if request.method == 'POST':
#        form = UserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            submitted = True
#
#            return render(request, "testapp/userform.html", {"form":form, "message":"Record Submitted Successfully"})
#        else:
#            return render(request, "testapp/userform.html", {"form":form, "message":"Record Submitted Successfully"})
#
#    return render(request,'testapp/userform.html', {'form':form, 'submitted':submitted})
#
# def Hire_view(request):
#    submitted=False
#    form = HireForm()
#    if request.method == 'POST':
#        form = HireForm(request.POST)
#        if form.is_valid():
#            form.save()
#            submitted=True
#
#            return render(request, "testapp/hireform.html", {"form":form, "message":"Record Submitted Successfully"})
#        else:
#            return render(request, "testapp/hireform.html", {"form":form, "message":"Record Submitted Successfully"})
#
#    return render(request,'testapp/hireform.html', {'form':form, 'submitted':submitted})
#
# def UserCreateView(CreateView):
#    model = User
#    fields = '__all__'
# def UserCreateView(CreateView):
#    model = Rental
#    fields = '__all__'
# def UserCreateView(CreateView):
#    model = Hire
#    fields = '__all__'
