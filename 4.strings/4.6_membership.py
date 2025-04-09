"""
in
not in
"""

#1st program
a = "Python is a high-level language" #Upper case 'P'ython
print("Python" in a)#True: Python 
print("python" in a)#False: python

#2nd program
email = 'email@123.com'

if '@' in email and '.com' in email:
    print('valid email')

else:
    print('invalid email')