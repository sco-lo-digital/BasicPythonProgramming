__author__ = 'sco-lo-pro'


#program for computing wage
hours = input('Please enter hours')

try:

    hours = float(hours)
    rate = float(input('Please enter rate'))

except:
    print('Please enter a number')

    #provision for time and a half if more than 40 hrs worked
    if hours>40:
        rate *=1.5

pay = hours * rate

print('Pay = ', str(pay))

