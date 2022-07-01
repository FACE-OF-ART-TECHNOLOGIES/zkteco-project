from datetime import datetime

def getLastMonth():
  now = datetime.now()

  month = int(now.strftime("%m"))
  year = int(now.strftime("%Y"))

  if(month == 1):
    month = 12
    year = year - 1
  else:
    month = month -1

  lastMonthDate = datetime(year, month,1)
  lastMonth = lastMonthDate.strftime("%Y-%m")

  return lastMonth

def getCurrentMonth():
  now = datetime.now()

  month = int(now.strftime("%m"))
  year = int(now.strftime("%Y"))

  monthDate = datetime(year, month, 1)

  currentMonth = monthDate.strftime("%Y-%m")

  return currentMonth