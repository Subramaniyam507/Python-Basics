import calendar

print ("learning calendar module")
#weekheader fumction returns the days in the week  
#weekheader(numofletters) here numofletter=no of characters of a name of a day you print
#suppose numofletters=3 then O/p will "Mon" if it is 2 o/p will be Mo 
print(calendar.weekheader(9)) 
#skips a line
print()
#returns the index of the day of the first day of the week i.e monday-0 tuesday-1
print(calendar.firstweekday())
print()
#this function returns entire calendar of a particular year(2020) of a particular month(12) and num of words of a day(3=mon or 9 monday)
print(calendar.month(2020,12,9))
#returns the calender of a month as 2d array or matrix of dates
print(calendar.monthcalendar(2020,12))
#returns the calendar of an entire year with all months 
print(calendar.calendar(2020))
# returns number of leap days within a range of year first parameter is inclusive and the 2nd parameter is exclusive so 2014 wont be included
print(calendar.leapdays(2000,2004))
#is a leap year or not return boolean
print(calendar.isleap(2000))

#refer datetime and time modules