from django.shortcuts import render
from django.http import HttpResponseRedirect
from details.forms import Profile_Form
from details.models import LoanDetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import arrow


def home(request):
    return render(request, 'home.html')


# Load Requesting
def loan_request(request):
    if request.method == 'POST':
        fo = Profile_Form(request.POST, request.FILES)
        if fo.is_valid():
            data = fo.cleaned_data
            if data["salary"] < 50000:
                # person will not get the loan
                data["is_allocated"] = False
            elif data["salary"]>=50000 and data["salary"]<=100000:
                rang = LoanDetails.objects.filter(salary__gte=50000, salary__lte=100000)
                if (len(rang)+1)%2==0:
                    # if person comes in even place, will get the loan
                    data["is_allocated"] = True
                    data["loan_sanction_date"] = arrow.now().to('Asia/Kolkata').date()
                    data["loan_paid"] = 0
                    data["due_amount"] = data["loan_amount"]
                    data["due_date"] = arrow.now().to('Asia/Kolkata').shift(months=12).date()
                else:
                    # if person comes in odd place, will not get the loan
                    data["is_allocated"] = False
            elif data["salary"] > 100000:
                # Loan imidiate approval
                data["is_allocated"] = True
                data["loan_sanction_date"] = arrow.now().to('Asia/Kolkata').date()
                data["loan_paid"] = 0
                data["due_amount"] = data["loan_amount"]
                data["due_date"] = arrow.now().to('Asia/Kolkata').shift(months=12).date()

            loan = LoanDetails.objects.create(**data)
            # User unique id
            loan.unique = "USER" + str(loan.id)
            loan.save()

            data = {
                'name': loan.name,
                'USER ID': loan.unique,
                'age': loan.age,
                'address': loan.address,
                'phone': loan.phone,
                'email': loan.email,
                'salary': loan.salary,
                'loan_amount': loan.loan_amount,
                'is_allocated': "YES" if loan.is_allocated == True else "No",
                'loan_sanction_date': loan.loan_sanction_date if loan.is_allocated == True else " ",
                'loan_paid': loan.loan_paid,
                'due_amount': loan.due_amount,
                'due_date': loan.due_date
            }

            return render(request, 'details.html', {'d': data})
        else:
            # print(str(fo.errors))
            # print("FORM NOT VALID")
            return HttpResponseRedirect('/loan_request')
        return HttpResponseRedirect('/')

    return render(request, 'loan_request.html')


# user detail and loan status
def user_detail(request):
    if request.method == 'POST':
        name = request.POST.dict().get("name",None)
        loan = LoanDetails.objects.get(unique = name)

        data = {
             # 'id': loan.id,
             'name': loan.name,
             'USER ID': loan.unique,
             'age': loan.age,
             'address': loan.address,
             'phone': loan.phone,
             'email': loan.email,
             'salary': loan.salary,
             'loan_amount': loan.loan_amount,
             'is_allocated': "YES" if loan.is_allocated == True else "No",
             'loan_sanction_date': loan.loan_sanction_date if loan.is_allocated == True else " ",
             'loan_paid': loan.loan_paid,
             'due_amount': loan.due_amount,
             'due_date': loan.due_date,
             }

        return render(request, 'details.html', {'d': data})

    return render(request, 'show_details.html')


# full detail of users for admin view
def full_details(request):
    loan = LoanDetails.objects.all()
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(loan, 8)
    try:
        loan_data = paginator.page(page)
    except PageNotAnInteger:
        loan_data = paginator.page(1)
    except EmptyPage:
        loan_data = paginator.page(paginator.num_pages)

    return render(request, 'full_details.html', {'d': loan_data})

# loan approval
def approve(request, id=None):

    if id is not None:
        # Loan Approval
        loan = LoanDetails.objects.get(id=id)
        loan.is_allocated = True
        loan.loan_sanction_date = arrow.now().to('Asia/Kolkata').date()
        loan.due_amount = loan.loan_amount
        loan.due_date = arrow.now().to('Asia/Kolkata').shift(months=12).date()
        loan.save()
    loan = LoanDetails.objects.all()
    return render(request, 'full_details.html', {'d': loan})
