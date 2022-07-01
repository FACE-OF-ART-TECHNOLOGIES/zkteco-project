from calendar import month
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta

from appuser.api_functions import apifun_getTodayHourAndOverTime, apifun_getTotalOvertimeMin, apifun_getTotalWorkingMin, \
    apifun_monthlyEarnings
from .models import EmployeeAdvancePayment, EmployeeSalaryPaments, HrEmployee, AttDayDetails, NewAppSalary

from django.http import JsonResponse
from .extra_functions import getCurrentMonth, getLastMonth
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'apps/login/index.html',
                          {'error': "<strong>Login Failed! </strong>Given credentials is not correct."})
    else:
        return render(request, 'apps/login/index.html')


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def statistics(request):
    totalEmployees = HrEmployee.objects.all().count
    # Total Salary Paid
    totalSalaryPaid = EmployeeSalaryPaments.objects.all()
    salarypaid = 0

    for paid in totalSalaryPaid:
        salarypaid = salarypaid + float(paid.paidamount)

    # Total Advance Paid
    advancepaidamount = 0
    totalAdvancePaid = EmployeeAdvancePayment.objects.all()

    for advp in totalAdvancePaid:
        advancepaidamount = advancepaidamount + float(advp.advanceamount)

    context = {
        "salarypaid": salarypaid,
        "advancepaid": advancepaidamount,
        "totalemployee": totalEmployees
    }

    return render(request, 'apps/dashboard/statistics.html', context)


@login_required(login_url='/login/')
def dashboard(request):
    employees = HrEmployee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'apps/dashboard/index.html', context)


@login_required(login_url='/login')
def attendance(request):
    dailydetails = AttDayDetails.objects.all().order_by('-att_date')[:150]
    context = {
        'dailydetails': dailydetails
    }

    return render(request, 'apps/dashboard/attendance.html', context)


def atsummary(requests):
    pass
    # TODO: Add daily summary if needed


@login_required(login_url='/login/')
def salary(request):
    salary = NewAppSalary.objects.all()
    context = {
        'salaries': salary
    }
    return render(request, 'apps/dashboard/salary-details.html', context)


@login_required(login_url='/login')
def salaryreports(request):
    records = EmployeeSalaryPaments.objects.filter().order_by('-paidtime')[0:1000]

    return render(request, 'apps/dashboard/salary-reports.html', {"records": records})


@login_required(login_url='/login/')
def employee(request):
    pass


@login_required(login_url='/login/')
def advancepayments(request):
    employees = HrEmployee.objects.all()
    if (request.method == "POST"):
        employeeid = request.POST['employee']
        amount = request.POST['amount']
        if (employeeid and amount and int(amount) > 0):

            thismonth = getCurrentMonth()
            advance = EmployeeAdvancePayment()
            hremp = HrEmployee.objects.get(id=employeeid)
            advance.employee = hremp
            advance.advanceamount = int(amount)
            advance.month = thismonth
            advance.save()

            return render(request, 'apps/dashboard/advance-payments.html',
                          {'employees': employees, 'success': "Advance Record Added Successfully"})
        else:
            return render(request, 'apps/dashboard/advance-payments.html',
                          {'employees': employees, 'error': "Amount is required"})

    return render(request, 'apps/dashboard/advance-payments.html', {'employees': employees})


@login_required(login_url='/login/')
def payments(request):
    salary = NewAppSalary.objects.all()
    context = {
        'salaries': salary
    }
    return render(request, 'apps/dashboard/payments.html', context)


# @login_required(login_url='/login')
def totalapiworkinghour(request):
    user_id = request.GET["id"]
    min = apifun_getTotalWorkingMin(user_id)
    hour = min / 60
    context = {
        'status': 'success',
        'info': 'workinginfo',
        'hour': hour,
        'minutes': min,
        'user_id': user_id
    }
    return JsonResponse(context)


def totalapiovertimehour(request):
    user_id = request.GET["id"]
    min = apifun_getTotalOvertimeMin(user_id)
    hour = min / 60
    context = {
        'status': 'success',
        'info': 'overtimeinfo',
        'hour': hour,
        'minutes': min,
        'user_id': user_id
    }
    return JsonResponse(context)


def totalapimonthlyEarnings(request):
    user_id = request.GET["id"]
    earning = apifun_monthlyEarnings(user_id)
    context = {
        'status': 'success',
        'info': 'earnings',
        'type': 'monthly',
        'earnings': earning,
        'user_id': user_id
    }
    return JsonResponse(context)


def payApi(request):
    user_id = request.GET["id"]
    lastMonth = getLastMonth()

    user_id = request.GET["id"]
    emp = HrEmployee.objects.get(id=user_id)
    empSalary = NewAppSalary.objects.get(employee=emp)
    totalEarnings = float(apifun_monthlyEarnings(user_id))
    totalOvertime = apifun_getTotalOvertimeMin(user_id) / 60
    totalWorking = apifun_getTotalWorkingMin(user_id) / 60
    print("Employee Salary: " + str(empSalary.salary))

    advancepaid = 0
    try:
        advancepaid = EmployeeAdvancePayment.objects.get(employee=emp, month=lastMonth).advanceamount
    except:
        pass

    totalPayble = totalEarnings - float(advancepaid)

    isPaid = False
    paidTime = ''

    if getPaymentStatusOfUserPerMonth(user_id, lastMonth) == True:
        print("Salary already Paid")
        paidinfo = EmployeeSalaryPaments.objects.get(employee=emp, month=lastMonth)

        isPaid = True
        print("Paid Info", paidinfo.paidtime)
        paidTime = paidinfo.paidtime

    context = {
        'baseSalary': empSalary.salary,
        'empid': user_id,
        'advancepaid': advancepaid,
        'totalearnings': totalEarnings,
        'totalovertime': totalOvertime,
        'totalworkinghour': totalWorking,
        'totalpayable': totalPayble,
        'ispaid': isPaid,
        'paidtime': paidTime
    }

    return JsonResponse(context)


@login_required(login_url='/login/')
def pay(request):
    user_id = request.GET["id"]

    return render(request, 'apps/dashboard/pay.html', {'id': user_id})


@login_required(login_url='/login/')
@csrf_exempt
def api_marka_salary_as_paid(request):
    if request.method == "POST":
        month = getLastMonth()
        rcvamount = request.POST['totalpaybleamountrcv']
        print("From Views: " + rcvamount)
        empid = int(request.POST['empid'])
        workinghour = request.POST['workinghour']
        overtime = request.POST['overtime']
        advancetaken = request.POST['advancetaken']
        baseSalary = request.POST['basesalary']
        earnings = request.POST['earnings']
        if getPaymentStatusOfUserPerMonth(empid, month) == False:
            if HrEmployee.objects.get(id=empid) is not None:
                if rcvamount:
                    esp = EmployeeSalaryPaments()
                    employee = HrEmployee.objects.get(id=empid)
                    esp.employee = employee
                    esp.paidamount = rcvamount
                    esp.month = month
                    esp.workinghours = workinghour
                    esp.overtimehours = overtime
                    esp.advanceTaken = advancetaken
                    esp.baseSalary = baseSalary
                    esp.totalEarnings = earnings
                    esp.save()

                    success = {
                        "status": 'success',
                        "msg": "Salary Paid",
                        "user_id": empid,
                        "month": month,
                        "amount": rcvamount
                    }

                    return JsonResponse(success)
                else:
                    error = {
                        "status": 'error',
                        "msg": "Request data not valid"
                    }
                    return JsonResponse(error)
            else:
                error = {
                    "status": 'error',
                    "msg": 'Employee not found!'
                }

                return JsonResponse(error)
        else:
            error = {
                "status": 'error',
                "msg": 'Salary already Paid'
            }

            return JsonResponse(error)
    else:
        error = {
            "status": 'error',
            "msg": 'Request method not allowed!'
        }
        return JsonResponse(error)


# function
def getPaymentStatusOfUserPerMonth(user_id, month):
    emp = HrEmployee.objects.get(id=user_id)

    if EmployeeSalaryPaments.objects.filter(employee=emp, month=month).exists():
        return True  # Salary paid
    else:
        return False  # Salary Not Paid


@login_required(login_url='/login/')
def goto(request, id):
    return redirect('/pay?id=' + id)


@login_required(login_url='/login/')
def advancereports(request):
    advances = EmployeeAdvancePayment.objects.all()[0:1000]

    return render(request, 'apps/dashboard/advancereports.html', {'advances': advances})
