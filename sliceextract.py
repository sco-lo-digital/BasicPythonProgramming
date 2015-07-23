__author__ = 'sco-lo-pro'

#start with some text
text= "X-DSPAM-Confidence: 0.8475"
#we want to extract the numbers
#locate beginning of number by using white space
atpos= text.find(' ')
#add
number= text[atpos+1:]
#convert to float
number= float(number)
print(number)