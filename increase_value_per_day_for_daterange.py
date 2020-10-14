import locale
import datetime
import string
from datetime import timedelta, date

# Initialize 2 numeric values
i = 39.75
j = 39.75
initvalue = i

# Store today's date
x = datetime.datetime.now()
#print(x)

# Add days to a date
y = x + datetime.timedelta(days=32)
print('End date: ' + str(y))

# Subtract days from a date
z = x + datetime.timedelta(days=-30)
print('Start date: ' + str(z))
totaldays = y-z
print('Total amount of days in the range: ' + str(totaldays))

# Or simply set dates
# z = datetime(1988, 2, 19, 2, 12, 49)
# y = datetime(1988, 2, 19, 1, 56, 2)

# Increase numeric value with the other value, until day is the correct date
start_date = z
end_date = y
delta = timedelta(days=1)
while start_date < end_date:
    i = i+j
    start_date += delta

print('Initial value: ' + str(initvalue))
print('Value added per day: ' + str(j))
print('Final date reached in loop: ' + str(start_date))  
print('Final value: ' + str(i))



