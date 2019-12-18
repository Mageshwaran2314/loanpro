from django.shortcuts import render
from django.http import HttpResponseRedirect
from details.forms import details_form

from details.models import LoanDetails

import arrow

def home(request):
    return render(request, 'home.html')


def loan_request(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST.dict())
        fo = details_form(request.POST)
        if fo.is_valid():
            print(request.POST.dict())
            print(fo.cleaned_data)
            data = fo.cleaned_data
            d = {'name': 'MAGESHWARAN A', 'age': 43, 'phone': 9488359526, 'email': 'magesh.amtl@gmail.com',
             'salary': 3454566, 'loan_amount': 454564}

            if data["salary"] < 50000:
                data["is_allocated"] = False
            elif data["salary"]>=50000 and data["salary"]<=100000:
                print(data["salary"], type(data["salary"]))
                rang = LoanDetails.objects.filter(salary__gte=50000, salary__lte=100000)
                print(rang)
                if (len(rang)+1)%2==0:
                    data["is_allocated"] = True
                    data["loan_sanction_date"] = arrow.now().to('Asia/Kolkata').date()
                    data["loan_paid"] = 0
                    data["due_amount"] = data["loan_amount"]
                    data["due_date"] = arrow.now().to('Asia/Kolkata').shift(months=12).date()
                else:
                    data["is_allocated"] = False
            elif data["salary"] > 100000:
                data["is_allocated"] = True
                data["loan_sanction_date"] = arrow.now().to('Asia/Kolkata').date()
                data["loan_paid"] = 0
                data["due_amount"] = data["loan_amount"]
                data["due_date"] = arrow.now().to('Asia/Kolkata').shift(months=12).date()
            loan = LoanDetails.objects.create(**data)
            loan.unique = "USER" + str(loan.id)
            loan.save()

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
                'due_date': loan.due_date
            }

            return render(request, 'details.html', {'d': data})
        else:
            print(str(fo.errors))
            print("FORM NOT VALID")
            return HttpResponseRedirect('/loan_request')
        return HttpResponseRedirect('/')
    else:
        print("NOT A POST")
    return render(request, 'loan_request.html')


def user_detail(request):
    if request.method == 'POST':
        print(request.POST.dict())
        print(request.POST.dict().get("name",None))
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
             'due_date': loan.due_date
             }

        return render(request, 'details.html', {'d': data})

    return render(request, 'show_details.html')


def full_details(request):
    loan = LoanDetails.objects.all()
    return render(request, 'full_details.html', {'d': loan})


# def approve(request):
#
#     # if approve_loan is not None:
#     #     loan = LoanDetails.objects.get(id=approve_loan)
#     #     loan.is_allocated = True
#     #     loan.loan_sanction_date = arrow.now().to('Asia/Kolkata').date()
#     #     loan.due_amount = loan.loan_amount
#     #     loan.due_date = arrow.now().to('Asia/Kolkata').shift(months=12).date()
#     #     loan.save()
#     print("APROVE-------------------")
#     if request.method == 'GET':
#         id = request.GET.get('id')
#         loan = LoanDetails.objects.get(id=id)
#         loan.is_allocated = True
#         loan.loan_sanction_date = arrow.now().to('Asia/Kolkata').date()
#         loan.due_amount = loan.loan_amount
#         loan.due_date = arrow.now().to('Asia/Kolkata').shift(months=12).date()
#         loan.save()
#     loan = LoanDetails.objects.all()
#     return render(request, 'full_details.html', {'d': loan})

# def approve(request):
#     print("APROVE-------------------")
#     if request.method == 'POST':
#         id = request.GET.get('id')
#         loan = LoanDetails.objects.get(id=id)
#         loan.is_allocated = True
#         loan.loan_sanction_date = arrow.now().to('Asia/Kolkata').date()
#         loan.due_amount = loan.loan_amount
#         loan.due_date = arrow.now().to('Asia/Kolkata').shift(months=12).date()
#         loan.save()
#     loan = LoanDetails.objects.all()
#     return render(request, 'full_details.html', {'d': loan})


def approve(request, id=None):

    if id is not None:
        loan = LoanDetails.objects.get(id=id)
        loan.is_allocated = True
        loan.loan_sanction_date = arrow.now().to('Asia/Kolkata').date()
        loan.due_amount = loan.loan_amount
        loan.due_date = arrow.now().to('Asia/Kolkata').shift(months=12).date()
        loan.save()
    print("APROVE-------------------")
    loan = LoanDetails.objects.all()
    return render(request, 'full_details.html', {'d': loan})
