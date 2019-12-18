from django import forms


class details_form(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField()
    phone = forms.IntegerField()
    email = forms.CharField(max_length=60)
    salary = forms.IntegerField()
    loan_amount = forms.IntegerField()
    # profile = forms.FileField(null=True)
