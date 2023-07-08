from datetime import date
import calendar
mm=12
yy=5
# print(calendar.month(yy,mm))
today=(date.today())
# print('\ncurrent date',today.strftime('%d'),today.month,today.year)
res=calendar.monthrange(today.year,today.month)
# day=res[1]
# print("\nlast date of the month ",day,today.month,today.year,"\n")

# Get the current year and month
year = today.year
month = today.month
# Create a calendar object
cal = calendar.monthcalendar(year, month)

# Remove Sundays from the calendar
for week in cal:
    if week[6] !=0:
        week[6] = ""
a=[]
# Print the modified calendar
# print("this is calender of current month except Sundays\n")
for week in cal:
    for day in week:
        if day == "":
            pass
        elif(day==0):
            pass
        else:
            a.append(day)
        
# print(a)

def getCurDate():
    global today
    return [int(today.strftime('%d')),int(today.month),int(today.year)]

def getDates(month,year):
    # Create a calendar object
    cal = calendar.monthcalendar(year, month)

    # Remove Sundays from the calendar
    for week in cal:
        if week[6] !=0:
            week[6] = ""
    a=[]
    # Print the modified calendar
    # print("this is calender of current month except Sundays\n")
    for week in cal:
        for day in week:
            if day == "":
                pass
            elif(day==0):
                pass
            else:
                a.append(day)

    return a

def monthName(no):
    return calendar.month_name[no]
# print(monthName(1))

thisday = getCurDate()
# print(thisday)
datestr = f"{thisday[0]}-{thisday[1]}-{thisday[2]}"