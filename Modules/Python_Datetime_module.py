import datetime as dt

# This is used to take the current datetime of the region :
x= dt.datetime.now()

print("Century: ",x.strftime("%C"))
print("Year: ",x.year)
print("Month: ",x.strftime("%b")) # Short of month "DECEMBER"-> "DEC"
print("Day: ",x.strftime("%a")) # Short of day "MONDAY" -> "MON"
print("Hour: ",x.strftime("%I")) # Other format of hour 04 rather than 16
print("Minute: ",x.minute)
print("Second: ",x.second)
print("Microsecond: ",x.microsecond)
print("Time of day: ",x.strftime("%p")) # AM/PM

# The strftime() function's formats:
# Directive	Description	Example	
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	