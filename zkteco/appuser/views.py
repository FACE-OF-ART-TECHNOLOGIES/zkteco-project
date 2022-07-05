from django.db import connections
from calendar import month
from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from .forms import DatewiseView

from appuser.api_functions import apifun_getTodayHourAndOverTime, apifun_getTotalOvertimeMin, apifun_getTotalWorkingMin, \
    apifun_monthlyEarnings
from .models import USERINFO, EmployeeAdvancePayment, EmployeeSalaryPaments, HrEmployee, AttDayDetails, NewAppSalary, CHECKINOUT

from django.http import HttpResponse, JsonResponse
from .extra_functions import getCurrentMonth, getLastMonth
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware


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
    records = EmployeeSalaryPaments.objects.filter().order_by(
        '-paidtime')[0:1000]

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
        advancepaid = EmployeeAdvancePayment.objects.get(
            employee=emp, month=lastMonth).advanceamount
    except:
        pass

    totalPayble = totalEarnings - float(advancepaid)

    isPaid = False
    paidTime = ''

    if getPaymentStatusOfUserPerMonth(user_id, lastMonth) == True:
        print("Salary already Paid")
        paidinfo = EmployeeSalaryPaments.objects.get(
            employee=emp, month=lastMonth)

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


def fetch_data(request):

    # sql = 'Select * From USERINFO'
    # with connections['machine'].cursor() as cursor:

    #     cursor.execute(sql)
    #     row = cursor.fetchall()

    #     print(row)
    user_info_all = USERINFO.objects.using('machine').all()
    return HttpResponse(user_info_all)


def string_to_date(time_string):
    new_time_string = time_string[:19]
    datetime_object = datetime.strptime(
        new_time_string, "%Y-%m-%d %H:%M:%S").date()
    return datetime_object


def string_to_time(time_string):
    new_time_string = time_string[:19]
    datetime_object = datetime.strptime(
        new_time_string, "%Y-%m-%d %H:%M:%S").time()
    return datetime_object


@csrf_exempt
@login_required
def check_time(request):
    global sel_date, check_all_new
    hr_employee_all = HrEmployee.objects.all()

    # select_form = DatewiseView
    all_data = []
    format = "%Y-%m-%d %H:%M:%S"
    if request.method == "POST":
        sel_date = request.POST['sel_date']
        for em in hr_employee_all:
            if em.rf_id != '0':
                try:
                    em_user_info = USERINFO.objects.using(
                        'machine').get(BADGENUMBER=em.rf_id)
                except USERINFO.DoesNotExist:
                    pass
            
                # single_checkInOut = CHECKINOUT.objects.using('machine').filter(date_form=date_form.search_Day, USERID=em_user_info.USERID).order_by('CHECKTIME')
                # print(single_checkInOut)
                # em_checkInOut_final = []
                if em_user_info:
                    em_checkInOut = CHECKINOUT.objects.using('machine').filter(CHECKTIME__date=sel_date).filter(
                        USERID=em_user_info.USERID).order_by('CHECKTIME')
                    # for c in em_checkInOut:
                    #     em_checkInOut_new = string_to_date(str(c))
                    #     if str(em_checkInOut_new) == str(sel_date):
                    #         em_checkInOut_final.append({
                    #             'employee': em,
                    #             'em_user_info': em_user_info,
                    #             'em_checkInOut': c,
                    #             'em_checkInOut_new': em_checkInOut_new,
                    #             # 'check_In': string_to_time(str(c.first())),
                    #             # 'check_Out': string_to_time(str(c.last()))
                    #         })
                    if em_checkInOut:
                        w_checkout = str(em_checkInOut.last())
                        n_w_checkout = w_checkout[:19]
                        w_checkin = str(em_checkInOut.first())
                        n_w_checkin = w_checkin[:19]
                        all_data.append({
                            'employee': em,
                            'em_user_info': em_user_info,
                            'checkinout_date': string_to_date(str(em_checkInOut.first())),
                            'check_In': string_to_time(str(em_checkInOut.first())),
                            'check_Out': string_to_time(str(em_checkInOut.last())),
                            'working_hour': datetime.strptime(n_w_checkout, format) - datetime.strptime(n_w_checkin, format)
                        })
    # print(all_data)
    context = {
        'all_data': all_data
    }

    return render(request, 'apps/dashboard/check-in-out.html', context)
