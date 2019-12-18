from django import forms
from details.models import LoanDetails

class Profile_Form(forms.ModelForm):

    class Meta:
        model = LoanDetails
        fields = ("name", "age", "address", "phone", "email", "salary", "loan_amount", "profile")
