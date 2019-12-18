from django.db import models


class LoanDetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=60, null=True)
    salary = models.IntegerField(default=0)
    loan_amount = models.IntegerField(default=0)
    is_allocated = models.BooleanField(default=False)
    loan_sanction_date = models.DateField(null=True)
    loan_paid = models.IntegerField(default=0)
    due_amount = models.IntegerField(default=0)
    due_date = models.DateField(null=True)
    unique = models.CharField(max_length=50, null=True)
    profile = models.ImageField(null=True)

    class Meta:
        db_table = "loan_details"
