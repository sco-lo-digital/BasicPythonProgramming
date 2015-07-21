__author__ = 'sco-lo-pro'

#program for computing wage

hours = float(input('Please enter hours'))

rate = float(input('Please enter rate'))

#provision for time and a half if more than 40 hrs worked
if hours>40:
    rate *=1.5


pay = hours * rate
print('Pay = ', str(pay))