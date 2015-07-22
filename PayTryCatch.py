__author__ = 'sco-lo-digital'


#program for computing wage

#ask user for input hours
# #Try/Except
try:
    hours = float(input('Please enter hours'))
except ValueError:
    print('ERROR: Please enter valid number')
    quit()

#ask user for input rate
try:
    rate = float(input('Please enter rate'))
except ValueError:
    print('ERROR: Please enter a valid rate')
    quit()

#provision for time and a half if more than 40 hrs worked
if hours>40:
   rate *=1.5
#else normal rate
else: rate *=1
#calculate pay
pay = hours * rate
#print the result
print('Pay = ', str(pay))
print('Thank you for using sco-lo-digital wage calculator. Goodbye.')
quit()
