from django import template
from django.utils.translation import deactivate
from appuser.models import AttDayDetails, HrEmployee, AttPunches, NewAppSalary
from datetime import date, datetime, timedelta
from calendar import monthrange
from django.utils.dateparse import parse_datetime

register = template.Library()
# Functions
def apifun_isSameDateTime(datetime1, datetime2):
    if datetime1 == datetime2:
        print(str(datetime1) + ' == ' + str(datetime2))
    else:
        print(str(datetime1) + " Not Equal " + str(datetime2))

def apifun_getMonthRange(year, month):
    range = str(monthrange(year,month)).split(',')[1]
    range = int(range.replace(')', ''))
    return range

def apifun_getDay(datetime):
    return int(datetime.day)

def apifun_getDayName(datetime):
    return datetime.strftime('%A')

def apifun_getMonth(datetime):
    return int(datetime.month)

def apifun_getYear(datetime):
    return int(datetime.year)

def apifun_getCurrentMonth():
    # return int(datetime.now().month) - 1
    return 12

def apifun_getCurrentMonthRange():
    year = datetime.now().year
    month = datetime.now().month
    range = str(monthrange(2021,12)).split(',')[1]
    range = int(range.replace(')', ''))

    return range

def apifun_getCurrentYear():
    # return int(datetime.now().year)
    return 2021

def apifun_getCurrentDay():
    return int(datetime.now().day)

def apifun_getCurrentDayName():
    return str(datetime.now().strftime('%A'))

# Tags
def apifun_getTodayHourAndOverTime(user_id,date):
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

def apifun_getTotalWorkingMin(user_id):
    current_month = apifun_getCurrentMonth()
    monthRange = apifun_getCurrentMonthRange()
    current_year = apifun_getCurrentYear()

    totalMonthlyWorkingTime = 0

    for day in range(monthRange):
        tdate = datetime(current_year,current_month,day+1)
        try:
            if apifun_getTodayHourAndOverTime(user_id, tdate) is not None:
                # print("Current Time: " + str(getTodayHourAndOverTime(user_id, tdate)[0]))
                totalMonthlyWorkingTime += apifun_getTodayHourAndOverTime(user_id, tdate)[0]
        except:
            pass
    
    return (totalMonthlyWorkingTime)

def apifun_getTotalOvertimeMin(user_id):
    current_month = apifun_getCurrentMonth()
    monthRange = apifun_getCurrentMonthRange()
    current_year = apifun_getCurrentYear()

    totalOvertime = 0

    for day in range(monthRange):
        tdate = datetime(current_year,current_month,day+1)
        try:
            if apifun_getTodayHourAndOverTime(user_id, tdate) is not None:
                # print("Current Time: " + str(getTodayHourAndOverTime(user_id, tdate)[1]))
                totalOvertime += apifun_getTodayHourAndOverTime(user_id, tdate)[1]
        except:
            pass
    
    return (totalOvertime)


def apifun_monthlyEarnings(user_id):
    w = apifun_getTotalWorkingMin(user_id)
    o = apifun_getTotalOvertimeMin(user_id)

    # 11 hours per day 26 days = 17160 min

    ts = NewAppSalary.objects.get(employee_id=user_id).salary
    
    perminIncome = ts / 17160

    wi = w * perminIncome
    oi = o * perminIncome

    total = wi + oi 

    return "{:.2f}".format(total)