from appuser.views import employee
from .models import AttDayDetails, AttDaySummary, AttPunches
from datetime import datetime
from django.utils.dateparse import parse_datetime
from .models import HrEmployee, NewAppSalary
from datetime import timedelta

def getDailyWorkTime(user_id,date):
    targetDate = datetime.strftime(date,"%Y-%m-%d")
    UserdayDetails = AttDayDetails.objects.get(employee_id=user_id, att_date=date)
    checkin_time = UserdayDetails.checkin

    # checkout
    alltimesbyuser = AttPunches.objects.filter(employee_id=user_id).order_by('punch_time')

    checkout_time = ''

    for usertime in alltimesbyuser:
        looptime = datetime.strftime(usertime.punch_time,"%Y-%m-%d %H:%M:%S") 
        if targetDate in looptime:
            checkout_time = looptime

    checkout_time = parse_datetime(checkout_time)

    checkout_hour = datetime.strftime(checkout_time, '%H')
    checkout_menuite = datetime.strftime(checkout_time, '%M')
    checkout_sec = datetime.strftime(checkout_time, '%S')

    checkin_hour = datetime.strftime(checkin_time, '%H')
    checkin_menuite = datetime.strftime(checkin_time, '%M')
    checkin_sec = datetime.strftime(checkin_time, '%S')

    checkout =timedelta(hours = int(checkout_hour) , minutes=int(checkout_menuite), seconds=int(checkout_sec))
    checkin = timedelta(hours= int(checkin_hour) , minutes=int(checkin_menuite), seconds=int(checkin_sec))

    total_working_hours = checkout - checkin


    return total_working_hours

def getDailyOverTime(workinghours, requireworkinghours):
    if workinghours > requireworkinghours:
        return workinghours - requireworkinghours
    else:
        return 0

def getCheckinTime(user_id, date):
    targetDate = datetime.strftime(date,"%Y-%m-%d")
    UserdayDetails = AttDayDetails.objects.get(employee_id=user_id, att_date=date)
    checkin_time = UserdayDetails.checkin

    return checkin_time

def getCheckoutTime(user_id, date):
    targetDate = datetime.strftime(date,"%Y-%m-%d")
    UserdayDetails = AttDayDetails.objects.get(employee_id=user_id, att_date=date)
    checkin_time = UserdayDetails.checkin

    # checkout
    alltimesbyuser = AttPunches.objects.filter(employee_id=user_id).order_by('punch_time')

    checkout_time = ''

    for usertime in alltimesbyuser:
        looptime = datetime.strftime(usertime.punch_time,"%Y-%m-%d %H:%M:%S") 
        if targetDate in looptime:
            checkout_time = looptime

    checkout_time = parse_datetime(checkout_time)

    return checkout_time

def getUserTotalSalary(user_id):
    usersalary = NewAppSalary.objects.get(employee=user_id)
    return usersalary.salary

def getTodayHourAndOverTime(user_id,date):
    # Create date
    targetDate = datetime.strftime(date,"%Y-%m-%d")
    UserdayDetails = AttDayDetails.objects.get(employee_id=user_id, att_date=date)
    checkin_time = UserdayDetails.checkin

    # checkout
    alltimesbyuser = AttPunches.objects.filter(employee_id=user_id).order_by('punch_time')

    checkout_time = ''

    for usertime in alltimesbyuser:
        looptime = datetime.strftime(usertime.punch_time,"%Y-%m-%d %H:%M:%S") 
        if targetDate in looptime:
            checkout_time = looptime

    checkout_time = parse_datetime(checkout_time)

    if checkout_time is not None and checkin_time is not None:

        targetCheckInTime = datetime.strftime(checkin_time, '%H:%M')
        targetCheckoutTime = datetime.strftime(checkout_time, '%H:%M')
        # If not checked out
        if targetCheckInTime == targetCheckoutTime:
            return [0,0]

        # Checked out
        checkout_hour = datetime.strftime(checkout_time, '%H')
        checkout_menuite = datetime.strftime(checkout_time, '%M')
        checkout_sec = datetime.strftime(checkout_time, '%S')

        checkin_hour = datetime.strftime(checkin_time, '%H')
        checkin_menuite = datetime.strftime(checkin_time, '%M')
        checkin_sec = datetime.strftime(checkin_time, '%S')

        checkout =timedelta(hours = int(checkout_hour) , minutes=int(checkout_menuite), seconds=int(checkout_sec))
        checkin = timedelta(hours= int(checkin_hour) , minutes=int(checkin_menuite), seconds=int(checkin_sec))

        total_working_hours = checkout - checkin

        str_data = str(total_working_hours)

        hour = int(str_data.split(':')[0])
        menuite = int(str_data.split(':')[1])
        sec = int(str_data.split(':')[2])


        # Round hour if work more than or equal to 45 min
        if menuite >= 45:
            hour += 1
            menuite = 0
        
        # Round Menuite if work less than 20 min make it 0
        if menuite <= 20:
            menuite = 0

        # Round menuite if work more than 20 make it 30
        if menuite > 20 and menuite < 44:
            menuite = 30
        
        # Checking if overtiem availabe
        overtimeHour = 0
        overtimeMenuite = 0
        totalOvertimeMenuites = 0
        totalWorkingMenuites = 0

        # Overtime Calculation
        if(hour >= 11 and menuite > 20):
            if hour > 11:
                overtimeHour = hour - 11
            overtimeMenuite = menuite
        
        if overtimeHour > 0 or overtimeMenuite > 0:
            # result = str(overtimeHour) + " hour and " +  str(overtimeMenuite) + " min"
            totalOvertimeMenuites = (overtimeHour*60) + overtimeMenuite
        else:
            totalOvertimeMenuites = 0

        # Hour Calculation
        if(hour > 11):
            totalWorkingMenuites = (11 * 60)
        else:
            totalWorkingMenuites = (hour * 60) + menuite

        return [totalWorkingMenuites, totalOvertimeMenuites]
    else:
        return [0,0]       

def getTodayWorkingMin(user_id):
    today = datetime(2021,12,15)
    return getTodayHourAndOverTime(user_id, today)

 
    