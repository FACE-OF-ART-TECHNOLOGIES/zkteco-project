from django import template
from django.utils.translation import deactivate
from appuser.models import AttDayDetails, HrEmployee, AttPunches, NewAppSalary
from datetime import date, datetime, timedelta
from calendar import monthrange
from django.utils.dateparse import parse_datetime
from ..helper_functions import getDailyOverTime, getDailyWorkTime, getUserTotalSalary


register = template.Library()
# Functions
def isSameDateTime(datetime1, datetime2):
    if datetime1 == datetime2:
        print(str(datetime1) + ' == ' + str(datetime2))
    else:
        print(str(datetime1) + " Not Equal " + str(datetime2))

def getMonthRange(year, month):
    range = str(monthrange(year,month)).split(',')[1]
    range = int(range.replace(')', ''))
    return range

def getDay(datetime):
    return int(datetime.day)

def getDayName(datetime):
    return datetime.strftime('%A')

def getMonth(datetime):
    return int(datetime.month)

def getYear(datetime):
    return int(datetime.year)

def getCurrentMonth():
    return int(datetime.now().month)

def getCurrentMonthRange():
    year = datetime.now().year
    month = datetime.now().month
    range = str(monthrange(year,month)).split(',')[1]
    range = int(range.replace(')', ''))

    return range

def getCurrentYear():
    return int(datetime.now().year)

def getCurrentDay():
    return int(datetime.now().day)

def getCurrentDayName():
    return str(datetime.now().strftime('%A'))

# Tags

@register.simple_tag
def get_username_from_userid(user_id):
    try:
        fname = HrEmployee.objects.get(id=user_id).emp_firstname
        lname = HrEmployee.objects.get(id=user_id).emp_lastname
        fullname = fname + " " + lname
        return fullname
    except HrEmployee.DoesNotExist:
        return 'Unknown'

@register.simple_tag
def get_checkout_time(user_id, date, checkintime):
    totalworktime = getDailyWorkTime(user_id,date)
    
    totalSalary = getUserTotalSalary(user_id)
    print('User: ' + str(user_id) + " work time: " + str(totalworktime))
    # print("Total work time: " + str(totalworktime))
    # print("Total Salary : " + str(totalSalary))
    try:
        targetTime = datetime.strftime(checkintime, '%H:%M:%S')
        targetCheckInTime = datetime.strftime(checkintime, '%H:%M')

        # print("Target Time: " +  targetTime)

        datepattern = datetime.strftime(date,"%Y-%m-%d")
        # print ("My Selected Date: "+ datepattern)
       
        cehckoutTime = AttPunches.objects.filter(employee_id=user_id).order_by('punch_time')
        result = ''
        
        for mytimeobj in cehckoutTime:
            mystrtime = datetime.strftime(mytimeobj.punch_time,"%Y-%m-%d") 
            realtime = datetime.strftime(mytimeobj.punch_time,"%Y-%m-%d %H:%M:%S") 
            Targetrealtime = datetime.strftime(mytimeobj.punch_time,"%H:%M:%S") 
            if(datepattern in realtime ):
                result = realtime
       
        parsedResult = parse_datetime(result)
        # isSameDateTime(date,parsedResult)
        targetCheckoutTime = datetime.strftime(parsedResult, '%H:%M')
        # print("Target Checkout Time: " +  targetCheckoutTime)
        # isSameDateTime(targetCheckInTime, targetCheckoutTime)
        if targetCheckInTime == targetCheckoutTime:
            return "<p style='color:red'>Did not Checked Out</p>"
        if parsedResult is not None:
            # return parsedResult.strftime('%Y-%m-%d %I:%M %p')
            return parsedResult.strftime('%I:%M %p')
        else:
            return 'Absent'
    except AttPunches.DoesNotExist:
        return 'Unknown'

@register.simple_tag
def today_working_hour(user_id, date):
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
            return "0 hours, 0 min [NCO]"

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

        if menuite >= 45:
            hour += 1
            menuite = 0
        
        # Round Menuite if work less than 20 min make it 0
        if menuite <= 20:
            menuite = 0

        # Round menuite if work more than 20 make it 30
        if menuite > 20 and menuite < 45:
            menuite = 30

        result = str(hour) + " hours, " + str(menuite) + " min"

        # return str(total_working_hours)

        return result
    else:
        return "0 hours, 0 min"


# ====================
# @register.simple_tag
def getMonthlyIncome(user_id):
    # Daily working hour
    current_month = getCurrentMonth()
    current_year = getCurrentYear()
    current_month_range = getCurrentMonthRange()
    
    for index, x in range(1,current_month_range):
        create_date = str(current_year)+ '/' + str(current_month) + '/' + str(index)
        created_date = datetime.strptime(create_date, '%y-%m-%d')
        WorkAndOvertime = getTodayHourAndOverTime(user_id,created_date)
        working = WorkAndOvertime[0]
        overtime = WorkAndOvertime[1]

        print("User Id: "+ user_id + " Year: " + current_year + " Month: " + current_month + "Day: " + index + " Work: " + working + " over: " + overtime)

     
    # Employee Salary

    # Daily  Income

    # Daily Overtime Income

    # Total Income += Total Income
    # Total Income += Total

    return 0

@register.simple_tag
def getTodaysOverTime(user_id, date):
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
            return "0 hours, 0 min [NCO]"

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
        if(hour >= 11 and menuite > 20):
            if hour > 11:
                overtimeHour = hour - 11
            overtimeMenuite = menuite
        
        if overtimeHour > 0 or overtimeMenuite > 0:
            result = str(overtimeHour) + " hour and " +  str(overtimeMenuite) + " min"
        else:
            result = "0 hours, 0 min"

        return result
    else:
        return "0 hours, 0 min"

# Get hour and overtime array

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

@register.simple_tag
def getTodayWorkingMin(user_id):
    today = datetime(2021,12,15)
    return getTodayHourAndOverTime(user_id, today)

# @register.simple_tag
# def getTotalWorkingMin(user_id):
#     current_month = getCurrentMonth()
#     monthRange = getCurrentMonthRange()
#     current_year = getCurrentYear()

#     totalMonthlyWorkingTime = 0

#     for day in range(monthRange):
#         tdate = datetime(current_year,current_month,day+1)
#         try:
#             if getTodayHourAndOverTime(user_id, tdate) is not None:
#                 # print("Current Time: " + str(getTodayHourAndOverTime(user_id, tdate)[0]))
#                 totalMonthlyWorkingTime += getTodayHourAndOverTime(user_id, tdate)[0]
#         except:
#             pass
    
#     return (totalMonthlyWorkingTime)



# @register.simple_tag
# def getTotalOvertimeMin(user_id):
#     current_month = getCurrentMonth()
#     monthRange = getCurrentMonthRange()
#     current_year = getCurrentYear()

#     totalOvertime = 0

#     for day in range(monthRange):
#         tdate = datetime(current_year,current_month,day+1)
#         try:
#             if getTodayHourAndOverTime(user_id, tdate) is not None:
#                 # print("Current Time: " + str(getTodayHourAndOverTime(user_id, tdate)[1]))
#                 totalOvertime += getTodayHourAndOverTime(user_id, tdate)[1]
#         except:
#             pass
    
#     return (totalOvertime)

# @register.simple_tag
# def monthlyEarnings(user_id):
#     w = getTotalWorkingMin(user_id)
#     o = getTotalOvertimeMin(user_id)

#     # 11 hours per day 26 days = 17160 min

#     ts = NewAppSalary.objects.get(employee_id=user_id).salary
    
#     perminIncome = ts / 17160

#     wi = w * perminIncome
#     oi = o * perminIncome

#     total = wi + oi 


#     return "{:.2f}".format(total)