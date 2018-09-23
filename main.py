import spammer

delay = input('Enter the delay: ')
mobile = input('Enter the mobile number: ')
count = input('Enter the number of blasts: ')
s = spammer.Spammer(mobile, count, delay)
s.spam()
