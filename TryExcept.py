__author__ = 'sco-lo-pro'


inp = input('Enter Fahrenheit Temperature:')

#indentation is key to making this work
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print (cel)
except:
    print('Please enter a number')

