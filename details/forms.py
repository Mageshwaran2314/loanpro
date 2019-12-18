from django import forms
from details.models import LoanDetails


class details_form(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField()
    phone = forms.IntegerField()
    email = forms.CharField(max_length=60)
    salary = forms.IntegerField()
    loan_amount = forms.IntegerField()
    # profile = forms.ImageField()
    # profile = forms.FileField(null=True)


class Profile_Form(forms.ModelForm):

    class Meta:
        model = LoanDetails
        fields = ("name", "age", "address", "phone", "email", "salary", "loan_amount", "profile")
