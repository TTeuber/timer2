import re

time = input('time> ').replace(' ', '').lower()

# using Regex for pattern matching to parse time input
clockRegex = re.compile(r'(\d+)(:)?(\d\d)?(am|pm)?')  # hour : minute period
mo1 = clockRegex.search(time)
hour = int(mo1.group(1))  # assign hour
if type(mo1.group(3)) is str:  # assign minute if entered
    minute = int(mo1.group(3))
else:
    minute = 0
if type(mo1.group(4)) is str:  # assign 12hr am/pm or 24hr period 
    period = mo1.group(4)
    period_type = "12"
else:
    period = ''
    period_type = "24"

timer = input("timer> ").replace(' ', '')

# using Regex for pattern matching to parse timer input
timerRegex = re.compile(r'(\d+)(:)?(\d\d)?')  # hour : minute
mo2 = timerRegex.search(timer)
timer_hour = int(mo2.group(1))
if type(mo2.group(3)) is str:
    timer_minute = int(mo2.group(3))
else:
    timer_minute = 0

new_hour = hour + timer_hour
new_minute = minute + timer_minute
while new_minute > 59:
    new_minute -= 60
    new_hour += 1


def switch(am_pm):  #function for switching am/pm
    if am_pm == 'am':
        return 'pm'
    elif am_pm == 'pm':
        return 'am'

# formatting for 12hr or 24hr period type
if period_type == '12':
    while new_hour > 12:
        period = switch(period)
        new_hour -= 12
    if new_hour == 12 and (timer_hour != 0 or timer_minute != 0):  # correction for am/pm if final time is 12
        period = switch(period)
    if hour == 12 and (timer_hour != 0 or timer_minute != 0):  # correction for am/pm if initial time is 12
        period = switch(period)
else:
    while new_hour > 24:
        new_hour -= 24


print(f'{new_hour}:{new_minute:02d}{period}')
