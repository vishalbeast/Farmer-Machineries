from django import forms
from testapp.models import Rental
from testapp.models import User
from testapp.models import Hire
from crispy_forms import helper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):
    helper = helper.FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary w-100"))
    helper.form_action = "/user/"
    helper.form_method = "post"

    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "datetime": forms.DateInput(attrs={"type" : 'date'})
        }


class RentalForm(forms.ModelForm):
    helper = helper.FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary w-100"))
    helper.form_action = "/rental/"

    class Meta:
        model = Rental
        fields = "__all__"
        widgets = {
            "datetime": forms.DateInput(attrs={"type" : 'date'})
        }

class HireForm(forms.ModelForm):
    helper = helper.FormHelper()
    helper.add_input(Submit('submit', 'submit', css_class="btn btn-primary w-100"))
    helper.form_action = "/hire/"


    class Meta:
        model = Hire
        fields = "__all__"
        widgets = {
            "datetime": forms.DateInput(attrs={"type" : 'date'})
        }

